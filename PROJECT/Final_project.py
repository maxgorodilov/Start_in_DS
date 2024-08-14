import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
# Progress bar
import time
bar_p = st.progress(0)
for percentage_complete in range(100):
    time.sleep(0.1)
    bar_p.progress(percentage_complete + 1)

st.title('Аналитика заработной платы')
st.header('Часть 1')
st.subheader('Гостиницы и предприятия общественного питания без учета инфляции')
data2021 = pd.read_csv('https://raw.githubusercontent.com/maxgorodilov/Start_in_DS/main/HOTEL2021.csv')
data2022 = pd.read_csv('https://raw.githubusercontent.com/maxgorodilov/Start_in_DS/main/HOTEL2022.csv')
data2023 = pd.read_csv('https://raw.githubusercontent.com/maxgorodilov/Start_in_DS/main/HOTEL2023.csv')


st.subheader('График динамики зарплаты за каждый год')
fig, axes = plt.subplots(nrows=3, ncols=1, sharex=True, figsize=(10, 8))
for i, df in enumerate([data2021,data2022, data2023]):
    df.plot(x='month', y='salary', kind='line', ax=axes[i])
    axes[i].set_title(f'Динамика зарплаты за {i+2021} год')
st.pyplot(fig)


st.subheader('График динамики зарплаты за 3 года')
fig, ax = plt.subplots(figsize=(10, 8))
df_all_years = pd.concat([data2021, data2022, data2023], ignore_index=True)
df_all_years.plot(x='month', y='salary', kind='line', ax=ax)
ax.set_title('Динамика зарплаты за 2021-2023 гг.')
st.pyplot(fig)
st.markdown('**Вывод:Зарплаты в сфере гостиниц и предприятий \n общественного питания за последние 3 года \n (2021-2023) выросли с 30 тысяч рублей \n до 50 тысяч рублей. \n Рост был постепенный с течением времени**')


st.header('Часть 2')
st.subheader('Сфера образования без учета инфляции')
edu2021 = pd.read_csv('https://raw.githubusercontent.com/maxgorodilov/Start_in_DS/main/Eduction2021.csv')
edu2022 = pd.read_csv('https://raw.githubusercontent.com/maxgorodilov/Start_in_DS/main/Education2022.csv')
edu2023 = pd.read_csv('https://raw.githubusercontent.com/maxgorodilov/Start_in_DS/main/Education2023.csv')


st.subheader('График динамики зарплаты за каждый год')
fig, axes = plt.subplots(nrows=3, ncols=1, sharex=True, figsize=(10, 8))
for i, df in enumerate([edu2021,edu2022, edu2023]):
    df.plot(x='month', y='salary', kind='line', ax=axes[i])
    axes[i].set_title(f'Динамика зарплаты за {i+2021} год')
st.pyplot(fig)


st.subheader('График динамики зарплаты за 3 года')
fig, ax = plt.subplots(figsize=(10, 8))
df_all_years = pd.concat([edu2021, edu2022, edu2023], ignore_index=True)
df_all_years.plot(x='month', y='salary', kind='line', ax=ax)
ax.set_title('Динамика зарплаты за 2021-2023 гг.')
st.pyplot(fig)
st.markdown('**Вывод:с 2021 года по 2023 год зарплата в сфере образования \n подвержена колебаниям в диапозоне от 30 тысяч до более 70 тысяч рублей.\n  В течении каждого года зарпалата имеет тенденцию подниматься,\n но не сохраняется на высоких позициях \n и следующий год начинается снова с зарплаты едва привышающий предыдущий год.\n Самая большая зарплата наблюдается в июне. \n Для понимания причин таких колибаний нужно \n будет проводить более глубокую аналитику этой сферы.**')


st.header('Часть 3')
st.subheader('Сфера гостиниц C учетом инфляции')
infl=pd.read_csv('https://raw.githubusercontent.com/maxgorodilov/Start_in_DS/main/INFLIATION.csv')
# Объединение данных о зарплате В СФЕРЕ ГОСТИНИЦ И ПРЕДПРИЯТИЙ ОБЩЕСТВЕННОГО ПИТАНИЯ и инфляции
comb = pd.merge(data2021, infl, on='month', how='left')
comb1 = pd.merge(data2022, infl, on='month', how='left')
comb2 = pd.merge(data2023, infl, on='month', how='left')
#СОЗДАНИЕ НОВОЙ КОЛОНКИ С РАСЧЕТОМ ЗАРПЛАТЫ ПОСЛЕ ВЫЧИТА ИНФЛЯЦИИ
comb['salary_with_inflation'] = comb['salary'] -(comb['salary']/100 * comb['inf2021'])
comb1['salary_with_inflation'] = comb1['salary'] -(comb1['salary']/100 * comb1['inf2022'])
comb2['salary_with_inflation'] = comb2['salary'] -(comb2['salary']/100 * comb2['inf2023'])


st.subheader(' График роста зарплат с учетом инфляции по годам ')
fig, axes = plt.subplots(nrows=3, ncols=1, sharex=True, figsize=(10, 8))
for i, df in enumerate([comb,comb1, comb2]):
    df.plot(x='month', y='salary_with_inflation', kind='line', ax=axes[i])
    axes[i].set_title(f'Динамика зарплаты за {i+2021} год')
st.pyplot(fig)


st.subheader(' График роста зарплат с учетом инфляции за 3 года ')
fig, ax = plt.subplots(figsize=(10, 8))
df_all_years = pd.concat([comb,comb1, comb2], ignore_index=True)
df_all_years.plot(x='month', y='salary_with_inflation', kind='line', ax=ax)
ax.set_title('Динамика зарплаты с учетом инфляции 2021-2023 гг.')
st.pyplot(fig)
st.markdown('**Вывод:Учитывая уровень инфляции ,зарплаты в сфере гостиниц и \n предприятий лющественного питания так же растут**')



st.header('Часть 4')
st.subheader('Сфера образования C учетом инфляции')
#ДАННЫЕ ПО СФЕРЕ ОБРАЗОВАНИЯ И ИНФЛЯЦИИ
comb_edu = pd.merge(edu2021, infl, on='month', how='left')
comb1_edu = pd.merge(edu2022, infl, on='month', how='left')
comb2_edu = pd.merge(edu2023, infl, on='month', how='left')
comb_edu['salary_with_inflation'] = comb_edu['salary'] -(comb_edu['salary']/100 * comb_edu['inf2021'])
comb1_edu['salary_with_inflation'] = comb1_edu['salary'] -(comb1_edu['salary']/100 * comb1_edu['inf2022'])
comb2_edu['salary_with_inflation'] = comb2_edu['salary'] -(comb2_edu['salary']/100 * comb2_edu['inf2023'])
fig, axes = plt.subplots(nrows=3, ncols=1, sharex=True, figsize=(10, 8))


st.subheader('График роста зарплат с учетом инфляции по годам ')
for i, df in enumerate([comb,comb1, comb2]):
    df.plot(x='month', y='salary_with_inflation', kind='line', ax=axes[i])
    axes[i].set_title(f'Динамика зарплаты за {i+2021} год')
st.pyplot(fig)


st.subheader('График роста зарплат с учетом инфляции за 3 года ')
fig, ax = plt.subplots(figsize=(10, 8))
df_all_years = pd.concat([comb_edu,comb1_edu, comb2_edu], ignore_index=True)
df_all_years.plot(x='month', y='salary_with_inflation', kind='line', ax=ax)
ax.set_title('Динамика зарплаты с уччетом инфляции 2021-2023 гг.')
st.pyplot(fig)
st.markdown('**Вывод: учитывая уровень инфляции, в течение года \n мы видим более плавный рост заработной платы. \n Но в годичных временых рамках мы так же наблюдаем колебания.**')

