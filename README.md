# Exploratory Data Analysis: Medical Appointment No-Shows

## Project Overview

This project explores a medical appointment dataset to understand patterns associated with missed hospital appointments.

Using Python and pandas, I performed exploratory data analysis (EDA) to examine appointment attendance, patient age groups, SMS reminders, and waiting times between scheduling and appointments.

The analysis identifies patterns in missed appointments and highlights areas that may deserve further investigation to help healthcare providers better understand appointment attendance.

This project was completed as part of my CodeAlpha Data Analytics Internship.


## Project Objectives

* Understand the structure of the dataset.
* Check for missing values and duplicate records.
* Investigate unusual patient ages and waiting times.
* Analyze appointment attendance patterns.
* Compare missed appointments across age groups and genders.
* Explore the relationship between SMS reminders and appointment attendance.
* Visualize findings using charts.

## Tools Used

* Python
* Pandas
* Matplotlib
* Visual Studio Code
* GitHub

## Dataset

The project uses the Medical Appointment No Shows dataset published by `joniarroba` on Kaggle.

The dataset contains 110,527 appointment records and 14 original columns.

The original dataset was retained without deleting or changing records during the data quality checks.

**Dataset source:** [Medical Appointment No Shows on Kaggle](https://www.kaggle.com/joniarroba/noshowappointments)

**Licence:** CC BY-NC-SA 4.0, as listed on the dataset page.

## Analysis Performed

1. Inspected the dataset structure and column names.
2. Checked for missing values and duplicate records.
3. Investigated unusual patient ages.
4. Calculated overall appointment attendance and missed appointment rates.
5. Compared attendance patterns by gender and age group.
6. Examined attendance among patients who did and did not receive SMS reminders.
7. Calculated waiting times between scheduling and appointment dates.
8. Investigated records with negative waiting times.
9. Compared missed appointment rates across waiting-time groups.
10. Created charts to present selected findings.

## Key Findings

## Key Findings

* **Overall attendance:** The dataset contains 110,527 medical appointments. Of these, 88,208 appointments were attended and 22,319 were missed. The overall missed appointment rate was approximately 20.19%.

* **Age groups:** Patients aged 18–35 had the highest missed appointment rate at approximately 23.82%, while patients aged 56–75 had the lowest rate at approximately 15.53%.

* **SMS reminders:** Appointments with an SMS reminder had a higher missed appointment rate (27.57%) than appointments without a reminder (16.70%). This is an observed association and does not prove that SMS reminders cause missed appointments.

* **Waiting time:** The missed appointment rate was highest for appointments scheduled 31–90 days in advance, at approximately 33.16%. Same-day appointments had the lowest rate, at approximately 4.65%.

* **Data quality:** No missing values or duplicate records were identified in the checks performed. However, the dataset contained one negative age and seven records with ages above 100, which require further investigation.


## Visualizations

The project generates three charts:

### 1. Missed Appointments by Age Group
![Missed Appointments by Age Group](missed_appointments_by_age.png)

File: `missed_appointments_by_age.png`

Compares missed appointment rates across patient age groups.

### 2. Missed Appointments by SMS Reminder
![Missed Appointments by SMS Reminder](missed_appointments_by_sms.png)

File: `missed_appointments_by_sms.png`

Compares missed appointment rates between patients who received SMS reminders and those who did not.

### 3. Missed Appointments by Waiting Time

File: `missed_appointments_by_waiting_time.png`
![Missed Appointments by Waiting Time](missed_appointments_by_waiting_time.png)

Compares missed appointment rates across different waiting-time groups.

## Data Quality and Limitations

* **Missing values:** The checks performed found no missing values in the dataset.
* **Duplicate records:** No duplicate records were identified in the checks performed.
* **Unusual ages:** One record contained an age of -1, and seven records had ages above 100. These values were flagged for further investigation rather than automatically changed or deleted.
* **Waiting times:** Five records had negative waiting times. These were excluded from the waiting-time comparison because they may reflect data-entry issues or inconsistencies in the recorded dates.
* **Interpretation:** The analysis identifies associations, not causes. For example, the higher missed appointment rate among patients who received SMS reminders does not mean the reminders caused missed appointments.
* **Limitations:** The findings are based on the available dataset and may not explain every reason patients miss appointments. Further investigation would be needed before using these results to make healthcare decisions.


## How to Run the Project

1. Install Python.

2. Install the required libraries:

   `pip install pandas matplotlib`

3. Download the original dataset from Kaggle.

4. Place `KaggleV2-May-2016.csv` in the project folder.

5. Open a terminal in the project folder.

6. Run the analysis:

   `python analysis.py`


## Skills Demonstrated

* Data inspection and exploration
* Data quality checks
* Data grouping and aggregation
* Percentage calculations
* Exploratory data analysis
* Data visualization
* Communicating findings
* Basic Python programming

## Conclusion

This exploratory data analysis helped identify patterns associated with missed medical appointments. The results showed differences in missed appointment rates across age groups and waiting times, as well as between appointments with and without SMS reminders.

The findings suggest that waiting time and patient characteristics may be useful areas for further investigation. However, these results show associations rather than causes, and additional analysis would be needed before making recommendations for healthcare practice.

Through this project, I gained practical experience using Python and pandas to inspect data, identify data quality issues, calculate attendance rates, and communicate findings through visualizations.

