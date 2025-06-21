-- ClickHouse DDL for database: baseball_1
-- Generated from: spider_data/database/baseball_1/baseball_1.sqlite

CREATE DATABASE IF NOT EXISTS baseball_1;

CREATE TABLE `baseball_1`.`all_star` (
    `player_id` Nullable(String),
    `year` Nullable(Int64),
    `game_num` Nullable(Int64),
    `game_id` Nullable(String),
    `team_id` Nullable(String),
    `league_id` Nullable(String),
    `gp` Nullable(Decimal64(2)),
    `starting_pos` Nullable(Decimal64(2))
)
ENGINE = MergeTree()
ORDER BY tuple();

CREATE TABLE `baseball_1`.`appearances` (
    `year` Nullable(Int64),
    `team_id` Nullable(String),
    `league_id` Nullable(String),
    `player_id` Nullable(String),
    `g_all` Nullable(Decimal64(2)),
    `gs` Nullable(Decimal64(2)),
    `g_batting` Nullable(Int64),
    `g_defense` Nullable(Decimal64(2)),
    `g_p` Nullable(Int64),
    `g_c` Nullable(Int64),
    `g_1b` Nullable(Int64),
    `g_2b` Nullable(Int64),
    `g_3b` Nullable(Int64),
    `g_ss` Nullable(Int64),
    `g_lf` Nullable(Int64),
    `g_cf` Nullable(Int64),
    `g_rf` Nullable(Int64),
    `g_of` Nullable(Int64),
    `g_dh` Nullable(Decimal64(2)),
    `g_ph` Nullable(Decimal64(2)),
    `g_pr` Nullable(Decimal64(2))
)
ENGINE = MergeTree()
ORDER BY tuple();

CREATE TABLE `baseball_1`.`manager_award` (
    `player_id` Nullable(String),
    `award_id` Nullable(String),
    `year` Nullable(Int64),
    `league_id` Nullable(String),
    `tie` Nullable(String),
    `notes` Nullable(Decimal64(2))
)
ENGINE = MergeTree()
ORDER BY tuple();

CREATE TABLE `baseball_1`.`player_award` (
    `player_id` Nullable(String),
    `award_id` Nullable(String),
    `year` Nullable(Int64),
    `league_id` Nullable(String),
    `tie` Nullable(String),
    `notes` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY tuple();

CREATE TABLE `baseball_1`.`manager_award_vote` (
    `award_id` Nullable(String),
    `year` Nullable(Int64),
    `league_id` Nullable(String),
    `player_id` Nullable(String),
    `points_won` Nullable(Int64),
    `points_max` Nullable(Int64),
    `votes_first` Nullable(Int64)
)
ENGINE = MergeTree()
ORDER BY tuple();

CREATE TABLE `baseball_1`.`player_award_vote` (
    `award_id` Nullable(String),
    `year` Nullable(Int64),
    `league_id` Nullable(String),
    `player_id` Nullable(String),
    `points_won` Nullable(Decimal64(2)),
    `points_max` Nullable(Int64),
    `votes_first` Nullable(Decimal64(2))
)
ENGINE = MergeTree()
ORDER BY tuple();

CREATE TABLE `baseball_1`.`batting` (
    `player_id` Nullable(String),
    `year` Nullable(Int64),
    `stint` Nullable(Int64),
    `team_id` Nullable(String),
    `league_id` Nullable(String),
    `g` Nullable(Int64),
    `ab` Nullable(Decimal64(2)),
    `r` Nullable(Decimal64(2)),
    `h` Nullable(Decimal64(2)),
    `double` Nullable(Decimal64(2)),
    `triple` Nullable(Decimal64(2)),
    `hr` Nullable(Decimal64(2)),
    `rbi` Nullable(Decimal64(2)),
    `sb` Nullable(Decimal64(2)),
    `cs` Nullable(Decimal64(2)),
    `bb` Nullable(Decimal64(2)),
    `so` Nullable(Decimal64(2)),
    `ibb` Nullable(Decimal64(2)),
    `hbp` Nullable(Decimal64(2)),
    `sh` Nullable(Decimal64(2)),
    `sf` Nullable(Decimal64(2)),
    `g_idp` Nullable(Decimal64(2))
)
ENGINE = MergeTree()
ORDER BY tuple();

CREATE TABLE `baseball_1`.`batting_postseason` (
    `year` Nullable(Int64),
    `round` Nullable(String),
    `player_id` Nullable(String),
    `team_id` Nullable(String),
    `league_id` Nullable(String),
    `g` Nullable(Int64),
    `ab` Nullable(Int64),
    `r` Nullable(Int64),
    `h` Nullable(Int64),
    `double` Nullable(Int64),
    `triple` Nullable(Int64),
    `hr` Nullable(Int64),
    `rbi` Nullable(Int64),
    `sb` Nullable(Int64),
    `cs` Nullable(Decimal64(2)),
    `bb` Nullable(Int64),
    `so` Nullable(Int64),
    `ibb` Nullable(Decimal64(2)),
    `hbp` Nullable(Decimal64(2)),
    `sh` Nullable(Decimal64(2)),
    `sf` Nullable(Decimal64(2)),
    `g_idp` Nullable(Decimal64(2))
)
ENGINE = MergeTree()
ORDER BY tuple();

CREATE TABLE `baseball_1`.`player_college` (
    `player_id` Nullable(String),
    `college_id` Nullable(String),
    `year` Nullable(Int64)
)
ENGINE = MergeTree()
ORDER BY tuple();

CREATE TABLE `baseball_1`.`fielding` (
    `player_id` Nullable(String),
    `year` Nullable(Int64),
    `stint` Nullable(Int64),
    `team_id` Nullable(String),
    `league_id` Nullable(String),
    `pos` Nullable(String),
    `g` Nullable(Int64),
    `gs` Nullable(Decimal64(2)),
    `inn_outs` Nullable(Decimal64(2)),
    `po` Nullable(Decimal64(2)),
    `a` Nullable(Decimal64(2)),
    `e` Nullable(Decimal64(2)),
    `dp` Nullable(Decimal64(2)),
    `pb` Nullable(Decimal64(2)),
    `wp` Nullable(Decimal64(2)),
    `sb` Nullable(Decimal64(2)),
    `cs` Nullable(Decimal64(2)),
    `zr` Nullable(Decimal64(2))
)
ENGINE = MergeTree()
ORDER BY tuple();

CREATE TABLE `baseball_1`.`fielding_outfield` (
    `player_id` Nullable(String),
    `year` Nullable(Int64),
    `stint` Nullable(Int64),
    `glf` Nullable(Decimal64(2)),
    `gcf` Nullable(Decimal64(2)),
    `grf` Nullable(Decimal64(2))
)
ENGINE = MergeTree()
ORDER BY tuple();

CREATE TABLE `baseball_1`.`fielding_postseason` (
    `player_id` Nullable(String),
    `year` Nullable(Int64),
    `team_id` Nullable(String),
    `league_id` Nullable(String),
    `round` Nullable(String),
    `pos` Nullable(String),
    `g` Nullable(Int64),
    `gs` Nullable(Decimal64(2)),
    `inn_outs` Nullable(Decimal64(2)),
    `po` Nullable(Int64),
    `a` Nullable(Int64),
    `e` Nullable(Int64),
    `dp` Nullable(Int64),
    `tp` Nullable(Int64),
    `pb` Nullable(Decimal64(2)),
    `sb` Nullable(Decimal64(2)),
    `cs` Nullable(Decimal64(2))
)
ENGINE = MergeTree()
ORDER BY tuple();

CREATE TABLE `baseball_1`.`hall_of_fame` (
    `player_id` Nullable(String),
    `yearid` Nullable(Int64),
    `votedby` Nullable(String),
    `ballots` Nullable(Decimal64(2)),
    `needed` Nullable(Decimal64(2)),
    `votes` Nullable(Decimal64(2)),
    `inducted` Nullable(String),
    `category` Nullable(String),
    `needed_note` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY tuple();

CREATE TABLE `baseball_1`.`home_game` (
    `year` Nullable(Int64),
    `league_id` Nullable(String),
    `team_id` Nullable(String),
    `park_id` Nullable(String),
    `span_first` Nullable(String),
    `span_last` Nullable(String),
    `games` Nullable(Int64),
    `openings` Nullable(Int64),
    `attendance` Nullable(Int64)
)
ENGINE = MergeTree()
ORDER BY tuple();

CREATE TABLE `baseball_1`.`manager` (
    `player_id` Nullable(String),
    `year` Nullable(Int64),
    `team_id` Nullable(String),
    `league_id` Nullable(String),
    `inseason` Nullable(Int64),
    `g` Nullable(Int64),
    `w` Nullable(Int64),
    `l` Nullable(Int64),
    `rank` Nullable(Decimal64(2)),
    `plyr_mgr` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY tuple();

CREATE TABLE `baseball_1`.`manager_half` (
    `player_id` Nullable(String),
    `year` Nullable(Int64),
    `team_id` Nullable(String),
    `league_id` Nullable(String),
    `inseason` Nullable(Int64),
    `half` Nullable(Int64),
    `g` Nullable(Int64),
    `w` Nullable(Int64),
    `l` Nullable(Int64),
    `rank` Nullable(Int64)
)
ENGINE = MergeTree()
ORDER BY tuple();

CREATE TABLE `baseball_1`.`player` (
    `player_id` Nullable(String),
    `birth_year` Nullable(Decimal64(2)),
    `birth_month` Nullable(Decimal64(2)),
    `birth_day` Nullable(Decimal64(2)),
    `birth_country` Nullable(String),
    `birth_state` Nullable(String),
    `birth_city` Nullable(String),
    `death_year` Nullable(Decimal64(2)),
    `death_month` Nullable(Decimal64(2)),
    `death_day` Nullable(Decimal64(2)),
    `death_country` Nullable(String),
    `death_state` Nullable(String),
    `death_city` Nullable(String),
    `name_first` Nullable(String),
    `name_last` Nullable(String),
    `name_given` Nullable(String),
    `weight` Nullable(Decimal64(2)),
    `height` Nullable(Decimal64(2)),
    `bats` Nullable(String),
    `throws` Nullable(String),
    `debut` Nullable(String),
    `final_game` Nullable(String),
    `retro_id` Nullable(String),
    `bbref_id` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY tuple();

CREATE TABLE `baseball_1`.`park` (
    `park_id` Nullable(String),
    `park_name` Nullable(String),
    `park_alias` Nullable(String),
    `city` Nullable(String),
    `state` Nullable(String),
    `country` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY tuple();

CREATE TABLE `baseball_1`.`pitching` (
    `player_id` Nullable(String),
    `year` Nullable(Int64),
    `stint` Nullable(Int64),
    `team_id` Nullable(String),
    `league_id` Nullable(String),
    `w` Nullable(Int64),
    `l` Nullable(Int64),
    `g` Nullable(Int64),
    `gs` Nullable(Int64),
    `cg` Nullable(Int64),
    `sho` Nullable(Int64),
    `sv` Nullable(Int64),
    `ipouts` Nullable(Decimal64(2)),
    `h` Nullable(Int64),
    `er` Nullable(Int64),
    `hr` Nullable(Int64),
    `bb` Nullable(Int64),
    `so` Nullable(Int64),
    `baopp` Nullable(Decimal64(2)),
    `era` Nullable(Decimal64(2)),
    `ibb` Nullable(Decimal64(2)),
    `wp` Nullable(Decimal64(2)),
    `hbp` Nullable(Decimal64(2)),
    `bk` Nullable(Int64),
    `bfp` Nullable(Decimal64(2)),
    `gf` Nullable(Decimal64(2)),
    `r` Nullable(Int64),
    `sh` Nullable(Decimal64(2)),
    `sf` Nullable(Decimal64(2)),
    `g_idp` Nullable(Decimal64(2))
)
ENGINE = MergeTree()
ORDER BY tuple();

CREATE TABLE `baseball_1`.`pitching_postseason` (
    `player_id` Nullable(String),
    `year` Nullable(Int64),
    `round` Nullable(String),
    `team_id` Nullable(String),
    `league_id` Nullable(String),
    `w` Nullable(Int64),
    `l` Nullable(Int64),
    `g` Nullable(Int64),
    `gs` Nullable(Int64),
    `cg` Nullable(Int64),
    `sho` Nullable(Int64),
    `sv` Nullable(Int64),
    `ipouts` Nullable(Int64),
    `h` Nullable(Int64),
    `er` Nullable(Int64),
    `hr` Nullable(Int64),
    `bb` Nullable(Int64),
    `so` Nullable(Int64),
    `baopp` Nullable(String),
    `era` Nullable(Decimal64(2)),
    `ibb` Nullable(Decimal64(2)),
    `wp` Nullable(Decimal64(2)),
    `hbp` Nullable(Decimal64(2)),
    `bk` Nullable(Decimal64(2)),
    `bfp` Nullable(Decimal64(2)),
    `gf` Nullable(Int64),
    `r` Nullable(Int64),
    `sh` Nullable(Decimal64(2)),
    `sf` Nullable(Decimal64(2)),
    `g_idp` Nullable(Decimal64(2))
)
ENGINE = MergeTree()
ORDER BY tuple();

CREATE TABLE `baseball_1`.`salary` (
    `year` Nullable(Int64),
    `team_id` Nullable(String),
    `league_id` Nullable(String),
    `player_id` Nullable(String),
    `salary` Nullable(Int64)
)
ENGINE = MergeTree()
ORDER BY tuple();

CREATE TABLE `baseball_1`.`college` (
    `college_id` Nullable(String),
    `name_full` Nullable(String),
    `city` Nullable(String),
    `state` Nullable(String),
    `country` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY tuple();

CREATE TABLE `baseball_1`.`postseason` (
    `year` Nullable(Int64),
    `round` Nullable(String),
    `team_id_winner` Nullable(String),
    `league_id_winner` Nullable(String),
    `team_id_loser` Nullable(String),
    `league_id_loser` Nullable(String),
    `wins` Nullable(Int64),
    `losses` Nullable(Int64),
    `ties` Nullable(Int64)
)
ENGINE = MergeTree()
ORDER BY tuple();

CREATE TABLE `baseball_1`.`team` (
    `year` Nullable(Int64),
    `league_id` Nullable(String),
    `team_id` Nullable(String),
    `franchise_id` Nullable(String),
    `div_id` Nullable(String),
    `rank` Nullable(Int64),
    `g` Nullable(Int64),
    `ghome` Nullable(Decimal64(2)),
    `w` Nullable(Int64),
    `l` Nullable(Int64),
    `div_win` Nullable(String),
    `wc_win` Nullable(String),
    `lg_win` Nullable(String),
    `ws_win` Nullable(String),
    `r` Nullable(Int64),
    `ab` Nullable(Int64),
    `h` Nullable(Int64),
    `double` Nullable(Int64),
    `triple` Nullable(Int64),
    `hr` Nullable(Int64),
    `bb` Nullable(Int64),
    `so` Nullable(Decimal64(2)),
    `sb` Nullable(Decimal64(2)),
    `cs` Nullable(Decimal64(2)),
    `hbp` Nullable(Decimal64(2)),
    `sf` Nullable(Decimal64(2)),
    `ra` Nullable(Int64),
    `er` Nullable(Int64),
    `era` Nullable(Decimal64(2)),
    `cg` Nullable(Int64),
    `sho` Nullable(Int64),
    `sv` Nullable(Int64),
    `ipouts` Nullable(Int64),
    `ha` Nullable(Int64),
    `hra` Nullable(Int64),
    `bba` Nullable(Int64),
    `soa` Nullable(Int64),
    `e` Nullable(Int64),
    `dp` Nullable(Decimal64(2)),
    `fp` Nullable(Decimal64(2)),
    `name` Nullable(String),
    `park` Nullable(String),
    `attendance` Nullable(Decimal64(2)),
    `bpf` Nullable(Int64),
    `ppf` Nullable(Int64),
    `team_id_br` Nullable(String),
    `team_id_lahman45` Nullable(String),
    `team_id_retro` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY tuple();

CREATE TABLE `baseball_1`.`team_franchise` (
    `franchise_id` Nullable(String),
    `franchise_name` Nullable(String),
    `active` Nullable(String),
    `na_assoc` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY tuple();

CREATE TABLE `baseball_1`.`team_half` (
    `year` Nullable(Int64),
    `league_id` Nullable(String),
    `team_id` Nullable(String),
    `half` Nullable(Int64),
    `div_id` Nullable(String),
    `div_win` Nullable(String),
    `rank` Nullable(Int64),
    `g` Nullable(Int64),
    `w` Nullable(Int64),
    `l` Nullable(Int64)
)
ENGINE = MergeTree()
ORDER BY tuple();

