SELECT d."teamId"::INTEGER, d."teamName", d."Elo_rank"
FROM 
    (
    SELECT c.*, ROW_NUMBER()
      OVER (PARTITION BY "teamId"
            ORDER BY "event_date" desc)
    FROM
        (
            SELECT a."event_date" as "event_date", a."homeTeam_team_id" as "teamId", a."homeTeam_team_name" as "teamName", a."homeTeam_team_id_new_rank" as "Elo_rank" FROM
              (SELECT *, ROW_NUMBER()
              OVER (PARTITION BY "homeTeam_team_id"
              ORDER BY "event_date" desc)
              FROM "FOOTBALLMATCHPREDICTIONS_team_elo_ranks") a
              WHERE a.ROW_NUMBER = 1
        UNION
            SELECT b."event_date" as "event_date", b."awayTeam_team_id" as "teamId", b."awayTeam_team_name" as "teamName", b."awayTeam_team_id_new_rank" as "Elo_rank" FROM
              (SELECT *, ROW_NUMBER()
              OVER (PARTITION BY "awayTeam_team_id"
              ORDER BY "event_date" desc)
              FROM "FOOTBALLMATCHPREDICTIONS_team_elo_ranks") b
              WHERE b.ROW_NUMBER = 1
        ) c
    ) d
WHERE d.ROW_NUMBER = 1