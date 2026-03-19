

## 🎯 Data Jobs Analysis Project 🚀

This project explores the **2023 Data Jobs dataset**, focusing on uncovering trends in **data-related roles in India**. Through structured analysis and visualization, it highlights how skills, demand, and salaries interact in the data job market.

The analysis covers:

* 📊 **Exploratory Data Analysis (EDA)** to understand the dataset
* 💼 Identifying the **most demanded skills** for top data roles
* 📈 Analyzing **skill trends** for Data Analysts in India
* 💰 Evaluating **salary vs skills relationships**
* 🎯 Finding the **most optimal skills** using scatterplot insights

This is a **portfolio-project** demonstrating real-world data analysis using Python, structured workflows, and clean project organization.

---

### **📌 Background 🌍**

The demand for data professionals has grown rapidly, making it essential to understand **which skills truly matter** in the job market. This project is built on a real-world dataset provided by **Luke Barousse** via **Hugging Face**, containing detailed job postings from 2023.

The dataset includes information on **job roles, locations, salaries, and required skills**, allowing for a comprehensive analysis of hiring trends in the data domain—especially within **India’s job market**.

By analyzing this data, the project aims to bridge the gap between **what employers demand** and **what candidates should learn**, helping aspiring data professionals make informed career decisions.

---

### **🛠️ Tools of the Trade ⚙️**

* 🐍 **Python**: The backbone of the analysis

  * **Pandas** → Data cleaning & manipulation
  * **Matplotlib** → Data visualization (monochrome styled charts 📊)
  * **Seaborn** → Enhanced statistical visuals

* 📓 **Jupyter Notebook**: Used for running analysis and documenting insights step-by-step

* 💻 **Visual Studio Code**: My go-to IDE for project structure, scripts, and version control

* 🌳 **Git & GitHub**: Version control and showcasing this project as a portfolio. 😎  



## **🧹 Data Cleanup & Preparation 🛠️**

Before diving into analysis, the dataset required some essential cleaning to ensure consistency and usability. To keep the workflow clean and reusable, I created a **custom Python module (`data_process.py`)** inside the `src/data_jobs` package.

This module handles key preprocessing steps:

* 🔄 Converting `job_posted_date` from string to **datetime format**
* 🧩 Transforming `job_skills` from stringified objects into **usable Python lists**

```python
def clean_date(df):
    df = df.copy()
    df['job_posted_date'] = pd.to_datetime(df['job_posted_date'])
    return df

def clean_skills(df):
    df = df.copy()
    df['job_skills'] = df['job_skills'].map(lambda x: literal_eval(x) if pd.notna(x) else x)
    return df
```

By modularizing these steps, the project maintains a **scalable and organized structure**, making it easy to reuse preprocessing logic across multiple notebooks 🚀

---
## **My Analysis📊**

### **Deep Dive: Exploratory Data Analysis (EDA) 🔍**

To kick things off, I explored **Data Analyst roles across India**, focusing on **job distribution by location**, hiring patterns, and key job attributes. This helps understand where opportunities are concentrated and what employers are offering.

#### 🌆 **Job Distribution Across Locations**

Initial analysis revealed that **major tech hubs** dominate job postings, with cities like **Bangalore, Hyderabad, and Mumbai** leading in demand. This highlights the geographical concentration of data opportunities in India 💼

#### 🧩 **Key Job Attributes (Work Flexibility & Benefits)**

The following visualization captures important aspects like **remote work availability, degree requirements, and health insurance offerings**:

<p align="center">
  <img src="_plots\1_output.png" width="80%">
</p>

```python

dict_columns = {
    'job_work_from_home':'Work from Home',
    'job_no_degree_mention':'Job Degree Req.',
    'job_health_insurance':'Health Insurance Offered'
}

for i, (column, title) in enumerate(dict_columns.items()):
    counts = df_DA_IN[column].value_counts().reindex([True, False], fill_value=0)
    
    ax[i].pie(
        counts,
        labels=counts.index.map({True: 'Yes', False: 'No'}),
        autopct='%1.1f%%',
        startangle=90,
        pctdistance=.85,
        wedgeprops={'width':0.4},
        colors=["#265974", "#D69928"]
    )
    
    ax[i].set_title(title, fontsize=14, fontweight='bold', color="#333333")

plt.suptitle('Vital Details in Data Analytics (IN)', fontsize=18, fontweight='bold')
```

📌 This chart highlights how common **remote roles**, **degree requirements**, and **benefits** are in Data Analyst jobs.

#### 🏢 **Top Companies Hiring Data Analysts in India**

To identify major recruiters, I analyzed job postings by company and visualized the **top hiring organizations** using a bar chart.

<p align="left">
  <img src="_plots\2_companies.png" width="80%">
</p>

```python
df_com_plot = df_DA_IN['company_name'].value_counts().head(10).to_frame()

sns.set_theme(style='ticks')

sns.barplot(data=df_com_plot, x='count', 
            y='company_name', hue='count', 
            palette='crest', legend=False)

sns.despine()
plt.title('Top Companies for Data Analytics Jobs in India', 
          fontstyle='italic')

plt.ylabel(' ')
plt.xlabel('Job Count', fontstyle='italic')
```

📊 This gives a clear picture of **which companies are actively hiring**, helping target job applications more strategically 🎯

---

### **🔥 Skill Power: Most In-Demand Skills for Top Roles 💼**

To understand what drives hiring, I analyzed the **top 3 most popular data roles in India** and identified the **most demanded skills** for each. This helps uncover what employers prioritize across different career paths 🚀

Instead of just counts, I used **skill percentage (%)** to normalize demand—making comparisons across roles more meaningful.

#### 📊 **Top Skills Across Popular Data Roles**

The following visualization shows the **probability of a skill appearing** in job postings for each role:

<p align="left">
  <img src="_plots\3_skills_in_roles.png" width="80%">
</p>

```python 

for i, job_title in enumerate(top_titles):
    df_plot = df_skills_perc[
        df_skills_perc['job_title_short'] == job_title
    ].head()
    
    sns.barplot(
        data=df_plot,
        x='skill_%',
        y='job_skills',
        ax=ax[i],
        hue='skill_count',
        palette='crest',
        legend=False
    )
    
    ax[i].set_title(job_title)
    ax[i].set_ylabel('')
    ax[i].set_xlabel('')
    ax[i].set_xlim(0, 80)
    ax[i].set_xticks([])

    for n, v in enumerate(df_plot['skill_%']):
        ax[i].text(v+1, n, f'{v}%', va='center')

ax[-1].set_xticks(range(0, 81, 10))
ax[-1].xaxis.set_major_formatter(
    plt.FuncFormatter(lambda x, pos: f'{int(x)}%')
)
ax[-1].set_xlabel('Skill Percent')

```

📌 This chart highlights how **core skills like SQL, Python, and visualization tools** consistently appear across roles, while some skills remain **role-specific**.

🎯 The takeaway? Focus on **high-frequency, cross-role skills** first, then specialize based on your target role 😎

---

### **📈 Skill Trends: Data Analyst Roles in India 🔍**

To understand how demand evolves over time, I analyzed the **monthly trend of key Data Analyst skills** in India. This reveals not just what’s important—but **when it’s most in demand** 📊  

<p align="left">
  <img src="_plots\4_skill_trend_monthly.png" width="100%">
</p>

#### 📊 **Monthly Skill Demand Insights**

The analysis highlights trends for core skills like **SQL, Python, Excel, Tableau, and Power BI** across the year.

* 🥇 **SQL** remains the most consistently demanded skill throughout the year, peaking around **May–October**
* 🐍 **Python** shows a steady rise, with noticeable spikes mid-year—indicating growing importance in analytics workflows
* 📊 **Excel** maintains strong demand, especially in **May, July, and October**, proving it’s still a core business tool
* 📉 **Tableau & Power BI** (visualization tools) show **fluctuating but increasing demand**, with peaks aligning with reporting-heavy periods
* 🚀 **October** stands out as a peak month where multiple skills hit high demand simultaneously

🎯 **Key Insight:**
While foundational skills like **SQL and Excel remain stable**, tools like **Python and BI platforms are gaining momentum**, signaling a shift toward more advanced and automated analytics 😎

---
### **💰 Salary Reality Check: Data Roles in India 🚀**

Let’s talk money 💼—this analysis compares how different **data roles are paid**, revealing clear patterns in earning potential.

<p align="center">
  <img src="_plots\5_boxplot_salary_distribution.png" width="100%" length="80%">
</p>

* 🤖 **Machine Learning Engineers** top the chart with the **highest earning potential**, reaching up to ~$260k+, showing how valuable advanced specialization is
* 🧠 **Data Scientists vs Data Analysts** → a clear jump exists, with Data Scientists earning noticeably higher median salaries than Analysts
* ⚙️ **Senior Data Engineers** have a strong **salary floor (~$150k)**, though some lower-end variation exists based on company/industry
* 💻 **Software Engineers** show **stable but lower ranges**, indicating more standardized pay compared to data roles
* 🎯 **$100k is the new baseline** — most data roles (DA, DS, DE, MLE) comfortably cross this median mark

🎯 **Key Insight:**
Data careers aren’t just in demand—they’re **high-paying**, especially as you move toward **specialized or senior roles** 😎

---

### **🎯 The Sweet Spot: Most Optimal Skills for Data Analysts 💡**

Not all skills are equal—some give you **higher salary + strong demand**, making them the *most optimal* to learn. This analysis balances both to find the **best ROI skills** for Data Analysts in India 🚀

#### 📊 **Skill vs Salary vs Demand**

The scatterplot below maps:

* **X-axis** → Skill demand (%)
* **Y-axis** → Median salary ($)
* 🎨 **Color** → Technology category

<p align="left">
  <img src="_plots\6_scatterplot_optimal_skills.png" width="100%">
</p>

```python
from adjustText import adjust_text

sns.scatterplot(data=df_plot, x='skill_percent', y='median_salary',
                hue='technology')

texts = []
for i, txt in enumerate(df_plot.skills):
    texts.append(plt.text(
        df_plot['skill_percent'].iloc[i], 
        df_plot['median_salary'].iloc[i], 
        txt
    ))

adjust_text(texts, arrowprops=dict(arrowstyle='->', color='black'))

plt.xlim(0, 12)

plt.gca().yaxis.set_major_formatter(plt.FuncFormatter(
    lambda y, pos: f'${int(y/1000)}k'))

plt.gca().xaxis.set_major_formatter(plt.FuncFormatter(
    lambda x, pos: f'{int(x)}%'))

```

#### 🔍 **Key Insights from the Analysis**

* 🥇 **SQL** → The ultimate winner: **highest demand (~11%) + strong salary (~$96k)** → must-have foundation

* 📊 **Excel** → High demand + solid pay → still a **core business skill**

* 🐍 **Python** → Balanced demand & salary → essential for scaling into advanced analytics

* 💰 **Power BI & Tableau** → Lower demand but **higher salaries (~$108k–$111k)** → high-value visualization tools

* ⚡ **Spark & Looker** → Niche skills with **top-tier salaries (~$111k)** → great for specialization

* ☁️ **Cloud (Azure, AWS)** → Moderate demand + good pay → becoming increasingly important

🎯 **Final Takeaway:**
Start with **SQL + Excel + Python (foundation)**, then level up with **BI tools or niche tech (Spark, Cloud)** to maximize salary growth 😎

---

## **🧠 What I Learned 🚀**

This project wasn’t just about analysis—it was about building **real-world data skills** end-to-end 💼

* 🧹 **Data Cleaning & Preparation** → Handling messy data, transforming columns, and building reusable modules
* 📊 **Strategic Skill Analysis** → Going beyond counts to analyze **demand %, trends, and salary impact**
* 🐍 **Advanced Python Usage** → Writing efficient code with **Pandas, Seaborn, Matplotlib**, and modular design
* 📈 **Data Visualization** → Creating clean, **monochromatic charts** with clear storytelling
* 🧠 **Analytical Thinking** → Turning raw data into **actionable career insights**

🎯 **Key Takeaway:**
I learned how to **think like a data analyst**—not just analyze data, but extract insights that actually matter 😎

---

## **💡 Key Insights That Matter 🚀**

Here’s a distilled view of the **most important takeaways** from the entire analysis—focused, actionable, and career-oriented 😎


#### **📊 Market & Hiring Trends (EDA)**

* 🏆 **Top Recruiters**: SAZ India & S&P Global dominate hiring (90+ jobs each)
* 🏦 **BFSI Leads**: Companies like JPMorgan & Wells Fargo show **banking is the biggest data employer**
* 🌍 **Diverse Demand**: Firms like PepsiCo & Maxgen prove opportunities go beyond tech & finance

---

#### **🔥 Skill Demand Insights**

* 🥇 **SQL = Non-Negotiable** → #1 skill across all roles (Analyst, Engineer, Scientist)

* 🐍 **Python = Power Skill** → essential for Data Scientists & Engineers

* ☁️ **AWS = Future Shift** → strong demand signals move toward **cloud-based analytics**

* 🎯 **Role Breakdown**:

  * Data Analysts → **SQL + Excel + Tableau (business focus)**
  * Data Engineers → **Spark + Azure (infrastructure heavy)**
  * Data Scientists → **Python + R (statistical depth)**

* 🚀 **Best Entry Stack** → **SQL + Python + Tableau**

---

#### **📈 Skill Trends Over Time**

* 🥇 **SQL dominates all year (~50–55%)** → truly indispensable
* 📊 **Power BI is the fastest-growing skill** → ~66% growth 📈
* ⚖️ **Python vs Excel** → similar demand, but Python spikes during hiring cycles
* 📉 **Tableau stays stable** → still a strong enterprise tool

---

#### **💰 Salary Insights**

* 🤖 **ML Engineers** → highest earning potential (up to ~$260k+)
* 🧠 **Data Scientists > Data Analysts** → clear salary jump
* ⚙️ **Senior Data Engineers** → strong salary floor (~$150k)
* 🎯 **$100k+ is standard** for most data roles

---

#### **🎯 Optimal Skills Strategy**

* 🥇 **SQL** → best mix of **high demand + solid salary**
* 📊 **Excel & Python** → strong foundational combo
* 💰 **Power BI, Tableau** → higher salary potential
* ⚡ **Spark, Cloud** → niche but **top-paying skills**

---

🎯 **Final Insight:**
To win in the data job market →
👉 **Start with SQL + Python + Excel**
👉 Then scale with **BI tools + Cloud/Niche tech**

That’s the **fastest path to high-demand + high-paying roles** 🚀

---

## **🏁 Conclusion 🎯**

The data job market in India is **skill-driven and high-paying**, with clear demand for the right tools and technologies.

By focusing on **strong fundamentals (SQL, Python, Excel)** and gradually moving into **BI tools and specialized skills**, you can position yourself for **better opportunities and higher salaries** 💼🚀

🎯 **Bottom line:** Learn smart, not just more—and align your skills with market demand 😎





