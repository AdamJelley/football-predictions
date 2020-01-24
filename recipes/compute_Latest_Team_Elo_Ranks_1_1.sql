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
                a."homeTeam_team_id" as "teamId", 
                a."homeTeam_team_name" as "teamName", 
                a."homeTeam_team_id_new_rank" as "Elo_rank", 
                a."player_id_home_new_rank_min" as "player_rank_min",
                a."player_id_home_new_rank_max" as "player_rank_max",
                a."player_id_home_new_rank_avg" as "player_rank_avg",
                a."player_id_home_new_rank_stddev" as "player_rank_stddev",
                a."player_id_home_concat" as "player_id_concat",
                a."home_player_0" as "player_0",
                a."home_player_1" as "player_1",
                a."home_player_2" as "player_2",
                a."home_player_3" as "player_3",
                a."home_player_4" as "player_4",
                a."home_player_5" as "player_5",
                a."home_player_6" as "player_6",
                a."home_player_7" as "player_7",
                a."home_player_8" as "player_8",
                a."home_player_9" as "player_9",
                a."home_player_10" as "player_10"
            FROM
              (SELECT *, ROW_NUMBER()
              OVER (PARTITION BY "homeTeam_team_id"
              ORDER BY "event_date" desc)
              FROM "FOOTBALLMATCHPREDICTIONS_team_player_ranks_joined") a
              WHERE a.ROW_NUMBER = 1
        UNION
            SELECT 
                b."event_date" as "event_date", 
                b."awayTeam_team_id" as "teamId", 
                b."awayTeam_team_name" as "teamName", 
                b."awayTeam_team_id_new_rank" as "Elo_rank",
                b."player_id_away_new_rank_min" as "player_rank_min",
                b."player_id_away_new_rank_max" as "player_rank_max",
                b."player_id_away_new_rank_avg" as "player_rank_avg",
                b."player_id_away_new_rank_stddev" as "player_rank_stddev",
                b."player_id_away_concat" as "player_id_concat",
                a."away_player_0" as "player_0",
                a."away_player_1" as "player_1",
                a."away_player_2" as "player_2",
                a."away_player_3" as "player_3",
                a."away_player_4" as "player_4",
                a."away_player_5" as "player_5",
                a."away_player_6" as "player_6",
                a."away_player_7" as "player_7",
                a."away_player_8" as "player_8",
                a."away_player_9" as "player_9",
                a."away_player_10" as "player_10"
            FROM
              (SELECT *, ROW_NUMBER()
              OVER (PARTITION BY "awayTeam_team_id"
              ORDER BY "event_date" desc)
              FROM "FOOTBALLMATCHPREDICTIONS_team_player_ranks_joined") b
              WHERE b.ROW_NUMBER = 1
        ) c
    ) d
WHERE d.ROW_NUMBER = 1