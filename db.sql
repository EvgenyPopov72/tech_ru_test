--
CREATE DATABASE tech_ru_test;

CREATE EXTENSION "uuid-ossp";

-- Таблица регионов (стран)
CREATE TABLE regions
(
    -- PK, идентификатор региона
    id uuid NOT NULL PRIMARY KEY,
    -- Код региона
    code text NOT NULL,
    -- Название региона
    description text NOT NULL
);

-- Таблица валют
CREATE TABLE currencies
(
    -- PK, идентификатор валюты
    id uuid PRIMARY KEY NOT NULL,
    -- ISO код валюты
    iso_code integer NOT NULL,
    -- Знак валюты
    ticker text NOT NULL,
    -- Название валюты
    description text NOT NULL,
    -- FK, код региона валюты
    region_id uuid NOT NULL CONSTRAINT currencies_regions_fkey REFERENCES regions (id)
);

-- Таблица счетов (аккаунтов)
CREATE TABLE accounts
(
    -- PK, идентификатор аккаунта
    id uuid NOT NULL PRIMARY KEY,
    -- email
    email text NOT NULL UNIQUE,
    -- Номер мобильного телефона в форме 79265952625
    mobN text NOT NULL UNIQUE,
    -- Индекс компании с которой заключен договор
    agent text NOT NULL,
    -- Номер договора с агентом
    contract text NULL,
    -- Статус аккаунта
    status boolean NOT NULL default TRUE,
    -- Тип аккаунта
    type text NOT NULL default '???',
    -- Любые текстовые теги (получен скан паспорта, неплательщик, вип)
    tag text NULL,
    -- FK, Регион (страна) для которой создан аккаунт
    region_id uuid NOT NULL CONSTRAINT accounts_regions_fkey REFERENCES regions (id),
    -- FK, валюта счета
    currency_id uuid NOT NULL CONSTRAINT accounts_currencies_fkey REFERENCES currencies (id),
    -- Размер кредита доверия (овердрафт)
    trust_limit decimal default NULL,
    -- Лимит средств на одну транзакцию
    limit_per_transaction decimal default NULL,
    -- Лимит средств за сутки
    limit_per_day decimal default NULL
);
