import numpy as np

# Coefficients matrix A and constants vector b for a sample system of equations


# first variable is NET RATING
# second variable is Adjusted True Shooting
# third variable is SRS
# fourth variable is rORTG
# fifth variable is rDRTG 


A = np.array([
  
    # 2022-2023 NBA Season  
 
   [3.4, 2, 3.04, 2.8, -0.6], # Denver Nuggets - Ranked 1st (2022-2023) 
    [-0.3,- 0.7, -0.13, -1.8, -1.5], # Miami Heat - Ranked 2nd (2022-2023)
    [6.5, 1.9, 6.38, 3.2, -3.3], # Boston Celtics - Ranked 3rd (2022-2023)
    [0.6, .1, 0.43, -0.3, -0.9],     #  Los Angeles Lakers - Ranked 4th (2022-2023)
    [4.4, 2.7, 4.37, 2.9, -1.5],      # Philadelphia 76ers - Ranked 5th (2022-2023)
    [3.0, -0.4 , 2.99, 3, 0 ],      # New York Knicks - Ranked 6th (2022-2023)
    [2.1, -1.1, 2.08, 0.3, -1.8],      # Phoenix Suns - Ranked 7th (2022-2023)
    [1.7, 1.9, 1.66, 1.3, -0.4],       #Golden State Warriors - Ranked 8th (2022-2023)
    [3.5, 0.2, 3.61, 0.6, -2.9],       #Milwaukee Bucks - Ranked 9th (2022-2023)
    [5.5, 0.9, 5.23, 1.3, -4.2],       #Cleveland Cavaliers - Ranked 10th (2022-2023)
    [3.9 ,-1.1, 3.6, 0.3, -3.6 ],       #Memphis Grizzlies - Ranked 11th (2022-2023)
    [2.6, 2.7, 2.3, 4.6, 2],      # Sacramento Kings - Ranked 12th (2022-2023)
    [0.9, 1.7, 1.03, 0.2, -0.7],       #Brooklyn Nets - Ranked 13th (2022-2023)
    [.5 ,0.7, 0.31, 0.2, -0.7],       #Los Angeles Clippers - Ranked 14th (2022-2023)
    [-.1, 1.1, -0.22 ,-1.1, -1],       #Minnesota Timberwolves - Ranked 15th (2022-2023)
    [0.3, -0.2, 0.32, 1.8, 1.5],      # Atlanta Hawks - Ranked 16th (2022-2023)
    [1.9, 0.1, 1.63, -0.4, -2.3],     # New Orleans Pelicans - Ranked 17th (2022-2023)
    [1.5, -2.6, 1.59, 0.7, -0.8],      # Toronto Raptors - Ranked 18th (2022-2023)
    [1.0, -1.1 ,0.96, 0.4, -0.6],      # Oklahoma City Thunder - Ranked 19th (2022-2023)
    [1.3, 0.6, 1.37, -1.3, -2.6],      # Chicago Bulls - Ranked 20th (2022-2023)
    [0.1, 1.8, -0.14, 2, 1.9],      # Dallas Mavericks - Ranked 21st (2022-2023)
    [-0.9, 0.3, -1.03, 1, 1.9],      # Utah Jazz - Ranked 22nd (2022-2023)
    [-3.1, 0, -2.91, -0.2, 2.9],      # Indiana Pacers - Ranked 23rd (2022-2023)
    [-1.2, 0.4, -1.06, -0.4, 0.8],      # Washington Wizards - Ranked 24th (2022-2023)
    [-2.6, -0.8, -2.39, -3.2, -0.6],      # Orlando Magic - Ranked 25th (2022-2023)
    [-4.0, 0.8, -3.96, 0, 4],      # Portland Trail Blazers - Ranked 26th (2022-2023)
    [-6.1, -3.1, -5.89, -5.6, 0.5],       #Charlotte Hornets - Ranked 27th (2022-2023)
    [-7.9, -2.7, -7.62 , -3.4, 4.5],      # Houston Rockets - Ranked 28th (2022-2023)
    [-9.8, -2.7, -7.73, -4.6, 5.2],      # San Antonio Spurs - Ranked 29th (2022-2023)
    [-8.2, -2, -9.82, -4.1, 4.1] ,     # Detroit Pistons - Ranked 30th (2022-2023)


    # 2021-2022 NBA Season

    [5.6 , 1.6 ,5.52 , 0.5, -5.1], # Golden State - Ranked 1st (2021-2022)
    [7.5 , 1.2 , 7.02 , 2.4, -5.1], # Boston Celtics - Ranked 2nd (2021-2022)
    [4.6 , 1.8 , 4.23 , 1.7, -2.9], # Miami Heat - Ranked 3rd (2021-2022)
    [3.4 , 0.6 , 3.12 , 0.8, -2.6], # Dallas Mavericks - Ranked 4th (2021-2022)
    [7.5 , 1.5 , 6.94 , 2.8, -4.7], # Phoneix Suns - Ranked 5th (2021-2022)
    [5.6 , -1.3 , 5.37 , 2.6, -3], # Memphis Grizzlies - Ranked 6th (2021-2022)
    [3.3 , 1.4 , 3.22 , 3.1, -0.2], # Milwaukee Bucks - Ranked 7th (2021-2022)
    [2.7 , 1.2 , 2.57 , 1.5, -1.2], # Philadelphia 76ers - Ranked 8th (2021-2022)
    [6.2 , 2.3 , 5.67 , 4.7, -1.5], # Utah Jazz - Ranked 9th (2021-2022)
    [2.4 , 2.4 , 2.16 , 2.5, 0.1], # Denver Nuggets - Ranked 10th (2021-2022)
    [2.4 , -2.3 , 2.38 , 0.9, -1.5], # Toronto Raptors - Ranked 11th (2021-2022)
    [-0.4 , 1.3 , -0.38 , 1.2, 1.6], # Chicago Bulls - Ranked 12th (2021-2022)
    [2.6 , 0.7 , 2.53 , 2.3, -0.3], # Minnesota Timberwolves - Ranked 13th (2021-2022)
    [0.8 , 1, 0.82 , 1.6, 0.8], # Brooklyn Nets - Ranked 14th (2021-2022)
    [1.6 , 1.5 , 1.55 , 4.5, 2.9], # Atlanta Hawks - Ranked 15th (2021-2022)
    [-1 , -0.9, -0.84 , 0, 1], # New Orleans Pelicans - Ranked 16th (2021-2022)
    [2.2 , 0.5, 2.04 , -0.1, -2.3], # Cleveland Caveliers - Ranked 17th (2021-2022)
    [0.4 , 0.6, 0.53 , 2.1, 1.7], # Charlotte Hornets - Ranked 18th (2021-2022)
    [0 , -0.2, 0.09 , -1.9, -1.9], # Los Angeles Clippers - Ranked 19th (2021-2022)
    [0.1 , -1, 0.02 , 0.4, 0.3], # San Antonio Spurs - Ranked 20th (2021-2022)
    [-0.1 , -1.6, -0.01 , -1.6, -1.5], # New York Knicks - Ranked 21st (2021-2022)
    [-3.4 , 0.2, -3.23 , -0.9, 2.5], # Washington Wizards - Ranked 22nd (2021-2022)
    [-3 , 0.1, -3.08 , -1.7, 1.3], # Los Angeles Lakers - Ranked 23rd (2021-2022)
    [-5.4 , -0.5, -5.26 , -2.1, 3.3], # Sacramento Kings - Ranked 24th (2021-2022)
    [-9.1 , -1.6, -8.55 , -4.2, 4.9], # Portland TrailBlazers - Ranked 25th (2021-2022)
    [-3.5, -0.2 , -3.26, 0.6, 4.1], # Indiana Pacers - Ranked 26th (2021-2022)
    [-8.2, -3.6 , -7.9, -7.4, 0.8], # Oklahoma City Thunder - Ranked 27th (2021-2022)
    [-7.8, -3.3 , -7.36, -6, 1.8], # Detroit Pistons - Ranked 28th (2021-2022)
    [-8, -2.8 , -7.67, -7.5, 0.5], # Orlando Magic - Ranked 29th (2021-2022)
    [-8.3 , -0.1,-8.26 , -3.6, 4.7], # Houston Rockets - Ranked 30th (2021-2022)







                                       

    # 2020-2021 NBA Season 

    [5.8 , 2.1 , 5.57 , 4.9 , -0.9],   # Milwaukee Bucks - Ranked 1st (2020-2021)
    [5.9 , 2.5 , 5.67 , 4.9 , -1],     # Phoenix Suns - Ranked 2nd (2020-2021)
    [6.4 , 2.7 , 6.02 , 5.3 , -1.1],   # LA Clippers - Ranked 3rd (2020-2021)
    [2.4 , 0.9 , 2.14 , 3.4 , 1],      # Atlanta Hawks - Ranked 4th (2020-2021)
    [9.3 , 2.5 , 8.97 , 5.3 , -4],       # Utah Jazz - Ranked 5th (2020-2021)
    [5.6 , 0.7 , 5.28 , 0.9 , -4.7],   # 76ers - Ranked 6th (2020-2021)
    [4.5 , 3.8 , 4.24 , 6 , 1.5],      # Brooklyn Nets - Ranked 7th (2020-2021)
    [5 , 1.6 , 4.82 , 4.8 , -0.2],     # Denver Nuggets - Ranked 8th (2020-2021)
    [2.4 , 1 , 2.26 , 3.1 , 0.7],       # Dallas Mavericks - Ranked 9th (2020-2021)
    [1.8 , 0.5 , 1.81 , 5.5 , 3.7],     # Portland Trail Blazers - Ranked 10th (2020-2021)
    [2.8 , -0.3 , 2.77 , -2.4 , -5.2],  # LA Lakers - Ranked 11th (2020-2021)
    [2.4 , -1.3 , 2.13 , -1.7 , -4.1],  # New York Knicks - Ranked 12th (2020-2021)
    [0 , 0.9 , -0.06 , -1.1 , -1.1],    # Miami Heat - Ranked 13th (2020-2021)
    [1 , -1.2 , 1.07 , -0.3 , -1.3],    # Memphis Grizzlies - Ranked 14th (2020-2021)
    [1.5 , 0.2 , 1.32 , 1.7 , 0.2],     # Celtics - Ranked 15th (2020-2021)
    [-1.8 , -0.3 , -1.85 , -1.1 , 0.7],      # Wizards - Ranked 16th (2020-2021)
    [1 , 1.1 , 1.1 , -1.2 , -2.2],           # Warriors - Ranked 17th (2020-2021)
    [0 , 0.3 , -0.13 , 0.1 , 0.1],        # Pacers - Ranked 18th (2020-2021)
    [-1.8 , 0.5 , -1.58 , -1.3 , 0.5],     # Spurs - Ranked 19th (2020-2021)
    [-1.9 , -0.8 , -1.94 , -1.4 , 0.5],    # Hornets - Ranked 20th (2020-2021)
    [-0.9 , 0.3 , -0.94 , -1.2 , -0.3],     # Bulls - Ranked 21st (2020-2021)
    [-0.3 , -0.2 , -0.2 , 1.2 , 1.5],       # Pelicans - Ranked 22nd (2020-2021)
    [-3.6 , 0.6 , -3.45 , 1.3 , 4.9],        # Kings - Ranked 23rd (2020-2021)
    [-0.5 , -0.5 , -0.54 , -0.3 , 0.2],     # Raptors - Ranked 24th (2020-2021)
    [-5.5 , -1.7 , -5.25 , -2.8 , 2.7],      # Timberwolves - Ranked 25th (2020-2021)
    [-8.6 , -2.9 , -8.19 , -6.5 , 2.1],    # Cavaliers - Ranked 26th (2020-2021)
    [-10.5 , -3.3 , -10.13 , -8.8 , 1.7],  # Thunder - Ranked 27th (2020-2021)
    [-9.4 , -4.5 , -9.02 , -7.2 , 2.2],      # Magic - Ranked 28th (2020-2021)
    [-4.5 , -1.6 , -4.38 , -4.3 , 0.2],     # Pistons - Ranked 29th (2020-2021)
    [-7.8 , -1.9 , -7.5 , -5.2 , 2.6],      # Rockets - Ranked 30th (2020-2021)


  # 2019-2020 NBA Season 

 [5.7, -4.3, 6.28, 1.4, .8],  # Lakers - Ranked 1st (2019-2020)
[3, 2.2, 2.59, 1.9, 0],  # Heat - Ranked 2nd (2019-2020)
[2.1, 0.2, 2.35, 2.5, 0.4],  # Denver Nuggets - Ranked 3rd (2019-2020)
[6.3, 0.5, 5.83, 2.7, -3.6,], # Celtics - Ranked 4th (2019-2020)
[9.5, 1.8, 9.41, 1.8, -7.7],  # Bucks - Ranked 5th (2019-2020)
[6.3, 1.2, 6.66, 3.3, -3],  # Clippers - Ranked 6th (2019-2020)
[6.1, 0.9, 5.97, 0.5, -5.6],  # Raptors - Ranked 7th (2019-2020)
[2.8, 1.3, 3.13, 2.3, -0.5],  # Rockets - Ranked 8th (2019-2020)
[2, 0, 1.63, -0.6, -2.6],  # Pacers - Ranked 9th (2019-2020)
[2, 0.8, 2.33, 0.2, -1.8],  # Thunder - Ranked 10th (2019-2020)
[2.4, 2, 2.52, 1.7, -0.7],  # Jazz - Ranked 11th (2019-2020)
[2.3, 0.1, 2.25, 0.7, -1.6],  # 76ers - Ranked 12th (2019-2020)
[5, 1.6, 4.87, 6.1, 1.1],  # Mavericks - Ranked 13th (2019-2020)
[-0.6, -1.1, -11.01, -1.7, -1.1],  # Nets - Ranked 14th (2019-2020)
[-1.1, 0.5, -0.61, 3.1, 4.2] , # Trailblazers - Ranked 15th (2019-2020)
[-1, -2.1, -0.93, -2.1, -1.1] , # Magic - Ranked 16th (2019-2020)
[-1.1, -0.4, -0.91, -1.4, -0.3],  # Grizzlies - Ranked 17th (2019-2020)
[0.3, 1.1, 0.56, 1.1, 0.8] , # Suns - Ranked 18th (2019-2020)
[-1.1, 0.7, -0.65, 1.8, 2.9],  # Spurs - Ranked 19th (2019-2020)
[-2, 0.1, -1.59, -0.4, 1.6] , # Kings - Ranked 20th (2019-2020)
[-1.2, 0.3, -0.55, 0.1, 1.3],  # Pelicans - Ranked 21st (2019-2020)
[-7, -2.6, -7.03, -4.3, 2.7],  # Hornets - Ranked 22nd (2019-2020)
[-4.6, -0.3, -5.24, 0.3, 4.9],  # Wizards - Ranked 23rd (2019-2020)
[-3.1, -1.8, -4, -3.9, -0.8] , # Bulls - Ranked 24th (2019-2020)
[-6.5, -3.4, -6.72, -4.1, 2.4],  # Knicks - Ranked 25th (2019-2020)
[-3.7, -0.4, -4.38, -1.6, 2.1] , # Pistons - Ranked 26th (2019-2020)
[-7.6, -1.1, -7.71, -3.4, 4.2] , # Hawks - Ranked 27th (2019-2020)
[-4.1, -1.4, -4.02, -2.5, 1.6] , # Timberwolves - Ranked 28th (2019-2020)
[-7.9, -1.2, -7.77, -3.1, 4.8] , # Cavaliers - Ranked 29th (2019-2020)
[-8.6, -2.5, -8.12, -5.4, 3.2] , # Warriors - Ranked 30th (2019-2020)                             


  
     

     ])
# Find the maximum value in each column
max_values = np.max(A, axis=0)

# Divide each element in each column by its maximum value
normalize_A = A / max_values

b = np.array([30,29,28,27,26,25,24,23,22,21,20,19,18,17,16,15,14,13,12,11,10,9,8,7,6,5,4,3,2,1,   
              30,29,28,27,26,25,24,23,22,21,20,19,18,17,16,15,14,13,12,11,10,9,8,7,6,5,4,3,2,1,                                                                               
              30,29,28,27,26,25,24,23,22,21,20,19,18,17,16,15,14,13,12,11,10,9,8,7,6,5,4,3,2,1,
              30,29,28,27,26,25,24,23,22,21,20,19,18,17,16,15,14,13,12,11,10,9,8,7,6,5,4,3,2,1,
             ])  
# Example constants vector for the first 3 equations

# Solve the system using least squares regression
x, residuals, _, _ = np.linalg.lstsq(normalize_A, b, rcond=None)

# Print the solution
print("Solution (x):", x)
print("Residuals:", residuals)



result = np.dot(normalize_A, x)
print(result)