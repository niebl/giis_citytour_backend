-- Database: giis

CREATE TABLE stories
(
    story_id int GENERATED ALWAYS AS IDENTITY,
    story_title varchar(255),
    story_description text,

    UNIQUE(story_id)
);

CREATE TABLE sites
(
    site_id int GENERATED ALWAYS AS IDENTITY,
    story int REFERENCES stories(story_id) ON DELETE SET NULL,

    coordinates point,
    site_index int,

    site_name text,
    short_desc text,
    long_desc text,
    short_story text,
    long_story text,
    image_url varchar(255),

    radius int,

    UNIQUE(site_id)
);

CREATE TABLE bibliography
(
    source_id int GENERATED ALWAYS AS IDENTITY,
    short_citation text,
    long_citation text,

    UNIQUE(source_id)
);

CREATE TABLE sources
(
    source_list_id int GENERATED ALWAYS AS IDENTITY,
    site_id int REFERENCES sites(site_id) ON DELETE SET NULL,
    source int REFERENCES bibliography(source_id) ON DELETE SET NULL,

    UNIQUE(source_list_id)
);

COPY stories FROM '/srv/default_data/data-stories.csv' DELIMITER ',' CSV HEADER;
COPY sites FROM '/srv/default_data/data-sites.csv' DELIMITER ',' CSV HEADER;
COPY bibliography FROM '/srv/default_data/data-bibliography.csv' DELIMITER ',' CSV HEADER;
COPY sources FROM '/srv/default_data/data-sources.csv' DELIMITER ',' CSV HEADER;

--CREATE ROLE giis_read LOGIN PASSWORD {'password'};
--GRANT CONNECT ON DATABASE giis TO giis_read;
--GRANT USAGE ON SCHEMA public TO giis_read;
--GRANT SELECT ON stories TO giis_read;
--GRANT SELECT ON sites TO giis_read;
--GRANT SELECT ON bibliography TO giis_read;
--GRANT SELECT ON sources TO giis_read;