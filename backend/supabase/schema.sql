-- Supabase-Schema für das Kontaktformular der Website alkawakibi.org
-- Im SQL-Editor von Supabase einmal ausführen.

create table if not exists public.kontaktanfragen (
    id           bigint generated always as identity primary key,
    erstellt_am  timestamptz  not null default now(),
    name         text         not null,
    email        text         not null,
    telefon      text,
    betreff      text         not null,
    nachricht    text         not null,
    einwilligung boolean      not null default false,
    quelle       text,                       -- welche Variante/Seite gesendet hat
    ip_hash      text,                       -- gekürzter Hash, keine Klartext-IP
    user_agent   text,
    status       text         not null default 'neu'
                 check (status in ('neu', 'in_bearbeitung', 'erledigt', 'spam'))
);

comment on table public.kontaktanfragen is
    'Nachrichten aus dem Kontaktformular der Vereinswebsite.';

create index if not exists kontaktanfragen_erstellt_am_idx
    on public.kontaktanfragen (erstellt_am desc);
create index if not exists kontaktanfragen_status_idx
    on public.kontaktanfragen (status);

-- Zeilenschutz: nur der service_role-Schlüssel (im Apps Script) darf schreiben,
-- niemand darf über die öffentliche API lesen.
alter table public.kontaktanfragen enable row level security;
revoke all on public.kontaktanfragen from anon, authenticated;

-- Aufräumhilfe: Anfragen, die länger als zwei Jahre erledigt sind, entfernen.
-- Bei Bedarf als geplanter Auftrag (pg_cron) einrichten.
create or replace function public.kontaktanfragen_aufraeumen()
returns integer
language plpgsql
security definer
set search_path = public
as $$
declare geloescht integer;
begin
    delete from public.kontaktanfragen
     where status = 'erledigt'
       and erstellt_am < now() - interval '2 years';
    get diagnostics geloescht = row_count;
    return geloescht;
end;
$$;
