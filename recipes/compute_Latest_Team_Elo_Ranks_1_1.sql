SELECT d."teamId"::INTEGER, d."teamName", d."Elo_rank", d."player_rank_min", d."player_rank_max", d."player_rank_avg", d."player_rank_stddev", d."player_id_concat"
FROM 
    (
    SELECT c.*, ROW_NUMBER()
      OVER (PARTITION BY "teamId"
            ORDER BY "event_date" desc)
    FROM
        (
            SELECT 
                a."event_date" as "event_date", 
                a."team_id_home" as "teamId", 
                a."homeTeam_team_name" as "teamName", 
                a."homeTeam_team_id_new_rank" as "Elo_rank", 
                a."player_id_home_new_rank_min" as "player_rank_min",
                a."player_id_home_new_rank_max" as "player_rank_max",
                a."player_id_home_new_rank_avg" as "player_rank_avg",
                a."player_id_home_new_rank_stddev" as "player_rank_stddev",
                a."player_id_home_concat" as "player_id_concat"
            FROM
              (SELECT *, ROW_NUMBER()
              OVER (PARTITION BY "team_id_home"
              ORDER BY "event_date" desc)
              FROM "FOOTBALLMATCHPREDICTIONS_player_team_elo_ranks_joined") a
              WHERE a.ROW_NUMBER = 1
        UNION
            SELECT 
                b."event_date" as "event_date", 
                b."team_id_away" as "teamId", 
                b."awayTeam_team_name" as "teamName", 
                b."awayTeam_team_id_new_rank" as "Elo_rank",
                b."player_id_away_new_rank_min" as "player_rank_min",
                b."player_id_away_new_rank_max" as "player_rank_max",
                b."player_id_away_new_rank_avg" as "player_rank_avg",
                b."player_id_away_new_rank_stddev" as "player_rank_stddev",
                b."player_id_away_concat" as "player_id_concat"
            FROM
              (SELECT *, ROW_NUMBER()
              OVER (PARTITION BY "team_id_away"
              ORDER BY "event_date" desc)
              FROM "FOOTBALLMATCHPREDICTIONS_player_team_elo_ranks_joined") b
              WHERE b.ROW_NUMBER = 1
        ) c
    ) d
WHERE d.ROW_NUMBER = 1