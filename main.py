import scraper
import combine_data
import regression
import statistics
import pandas as pd


# Scrape data
# scraper.sports_ref_scrape("https://www.sports-reference.com/cbb/play-index/psl_finder.cgi?request=1&match=combined&year_min=2002&year_max=2016&conf_id=&school_id=&class_is_fr=Y&class_is_so=Y&class_is_jr=Y&class_is_sr=Y&pos_is_g=Y&pos_is_gf=Y&pos_is_fg=Y&pos_is_f=Y&pos_is_fc=Y&pos_is_cf=Y&pos_is_c=Y&games_type=A&qual=&c1stat=g&c1comp=gt&c1val=20&c2stat=fg3a_per_g&c2comp=gt&c2val=1.5&c3stat=&c3comp=&c3val=&c4stat=&c4comp=&c4val=&order_by=pts&order_by_asc=&offset=", "july25ncaa.csv")
# scraper.sports_ref_scrape("https://www.basketball-reference.com/play-index/psl_finder.cgi?request=1&match=combined&type=totals&per_minute_base=36&per_poss_base=100&lg_id=NBA&is_playoffs=N&year_min=2003&year_max=2017&franch_id=&season_start=1&season_end=-1&age_min=0&age_max=99&shoot_hand=&height_min=0&height_max=99&birth_country_is=Y&birth_country=&birth_state=&college_id=&draft_year=&is_active=&debut_yr_nba_start=&debut_yr_nba_end=&is_hof=&is_as=&as_comp=gt&as_val=0&award=&pos_is_g=Y&pos_is_gf=Y&pos_is_f=Y&pos_is_fg=Y&pos_is_fc=Y&pos_is_c=Y&pos_is_cf=Y&qual=&c1stat=g&c1comp=gt&c1val=50&c2stat=mp_per_g&c2comp=gt&c2val=7&c3stat=fg3a&c3comp=gt&c3val=150&c4stat=&c4comp=&c4val=&c5stat=&c5comp=&c6mult=&c6stat=&order_by=fg3&order_by_asc=&offset=", "july25nba.csv")

# Combine data
# combine_data.filter_data("july25nba.csv", 0, "july25ncaa.csv", 0, "combined_data_jul25.csv")

# Do Regression analysis
# Run 300 iterations of training/testing split

file = "combined_data_jul25.csv"
data = pd.read_csv(file, index_col=0)

# preds = []
# vs35s = []
# vs_college = []
#
# for i in range(1, 500):
#
#     # Seperate data into training set and testing set
#     training_data, test_data = regression.split_data(data, 0.2)
#     print(len(test_data))
#
#     # Get coefficients from linear regression on training set
#     coeffs = regression.get_coefficients("NBA_3P_percent ~ threeP_percent + FT_percent", training_data)
#
#     # Make NBA 3pt% prediction, and compare results to 35% +/- 2.5% benchmark
#     prediction, vs35, vs_col = regression.predict(coeffs, test_data)
#
#     preds.append(prediction)
#     vs35s.append(vs35)
#     vs_college.append(vs_col)
#
# print(statistics.mean(preds))
# print(statistics.mean(vs35s))
# print(statistics.mean(vs_college))
#


# Get final coefficients and scatter plots


# training_data, test_data = regression.split_data(data, 0)
# regression.scatter_plot("threeP_percent", "NBA_3P_percent", training_data)
# regression.scatter_plot("FT_percent", "NBA_3P_percent", data)
# regression.scatter_plot("threePAG", "NBA_3P_percent", data)
#
# regression.print_regression_results("NBA_3P_percent ~ threeP_percent + FT_percent", data)


# regression.scatter_plot("threeP_percent", "NBA_3P_percent", training_data)
# regression.scatter_plot("FT_percent", "NBA_3P_percent", training_data)
# regression.scatter_plot("threePAG", "NBA_3P_percent", training_data)
#
coeffs = regression.get_coefficients("NBA_3P_percent ~ threeP_percent + FT_percent", data)
regression.predict(coeffs, data)


# Get data for 2017 draft class
# scraper.get_draft_class_ids("https://www.basketball-reference.com/draft/NBA_2017.html", "2017draft.csv")
# scraper.sports_ref_scrape("https://www.sports-reference.com/cbb/play-index/psl_finder.cgi?request=1&match=combined&year_min=2012&year_max=2017&conf_id=&school_id=&class_is_fr=Y&class_is_so=Y&class_is_jr=Y&class_is_sr=Y&pos_is_g=Y&pos_is_gf=Y&pos_is_fg=Y&pos_is_f=Y&pos_is_fc=Y&pos_is_cf=Y&pos_is_c=Y&games_type=A&qual=&c1stat=&c1comp=&c1val=&c2stat=&c2comp=&c2val=&c3stat=&c3comp=&c3val=&c4stat=&c4comp=&c4val=&order_by=fg_pct&order_by_asc=&offset=", "ncaa_last_5_years.csv")
# combine_data.filter_data('2017draft.csv', 2, 'ncaa_last_5_years.csv', 0, '2017draft_stats.csv')