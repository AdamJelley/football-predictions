SELECT d."playerId"::INTEGER, d."playerName", d."Elo_rank"
FROM 
    (
    SELECT c.*, ROW_NUMBER()
      OVER (PARTITION BY "playerId"
            ORDER BY "event_date" desc)
    FROM
        (
            SELECT a."event_date" as "event_date", a."player_id_home" as "playerId", a."player_home" as "playerName", a."player_id_home_new_rank" as "Elo_rank" FROM
              (SELECT *, ROW_NUMBER()
              OVER (PARTITION BY "player_id_home"
              ORDER BY "event_date" desc)
              FROM "FOOTBALLMATCHPREDICTIONS_player_elo_ranks") a
              WHERE a.ROW_NUMBER = 1
        UNION
            SELECT b."event_date" as "event_date", b."player_id_away" as "playerId", b."player_away" as "playerName", b."player_id_away_new_rank" as "Elo_rank" FROM
              (SELECT *, ROW_NUMBER()
              OVER (PARTITION BY "player_id_away"
              ORDER BY "event_date" desc)
              FROM "FOOTBALLMATCHPREDICTIONS_player_elo_ranks") b
              WHERE b.ROW_NUMBER = 1
        ) c
    ) d
WHERE d.ROW_NUMBER = 1