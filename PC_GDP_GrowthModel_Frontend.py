from tkinter import *
from tkinter.ttk import *
import PC_GDP_GrowthModel as  PC
root = Tk()
root.geometry('500x700')
root.title("GDP growth model using parallel processing")

countries_selected = []
c, c1, c2 = '', '', ''
last_row = 2


def submit_click():
    global c1, c2, countries_selected
    c1, c2 = n1.get(), n2.get()
    countries_selected.append(c1)
    countries_selected.append(c2)
    PC.main(countries_selected)
    root.destroy()
    


def choice_sel(*args):
    # print(*args)
    countries_selected.append(args[0].widget.get())


def add_country():
    global last_row, countries_selected

    lblselectsountry = Label(root, text="Select country :").grid(row=last_row, column=0, pady=15)
    n = StringVar()
    countries_list = Combobox(root, width=27, textvariable=n, values=country_names)
    countries_list.grid(row=last_row, column=1)
    countries_list.bind("<<ComboboxSelected>>", lambda event: choice_sel(event))

    last_row += last_row


if __name__ == '__main__':
    country_names = (
        'Afghanistan', 'Africa', 'Albania', 'Algeria', 'Angola', 'Antigua and Barbuda', 'Argentina', 'Armenia',
        'Aruba',
        'Asia', 'Asia, Central', 'Australia', 'Australia & New Zealand', 'Austria', 'Azerbaijan', 'Bahamas',
        'Bahrain',
        'Bangladesh', 'Barbados', 'Belarus', 'Belgium', 'Belize', 'Benin', 'Bhutan', 'Bolivia',
        'Bosnia and Herzegovina',
        'Botswana', 'Brazil', 'Brunei', 'Bulgaria', 'Burkina Faso', 'Burundi', 'Cambodia', 'Cameroon', 'Canada',
        'Cape Verde', 'Caribbean', 'Central African Republic', 'Central America', 'Central and Southern Asia',
        'Chad',
        'Channel Islands', 'Chile', 'China', 'Colombia', 'Comoros', 'Congo', 'Costa Rica', "Cote d'Ivoire",
        'Croatia',
        'Cuba', 'Curacao', 'Cyprus', 'Czechia', 'Democratic Republic of Congo', 'Denmark', 'Djibouti',
        'Dominican Republic',
        'Eastern Africa', 'Eastern and South-Eastern Asia', 'Eastern Asia', 'Eastern Europe', 'Ecuador', 'Egypt',
        'El Salvador', 'Equatorial Guinea', 'Eritrea', 'Estonia', 'Eswatini', 'Ethiopia', 'Europe',
        'Europe and Northern America', 'Europe, Western', 'Fiji', 'Finland', 'France', 'French Guiana',
        'French Polynesia',
        'Gabon', 'Gambia', 'Georgia', 'Germany', 'Ghana', 'Greece', 'Grenada', 'Guadeloupe', 'Guam', 'Guatemala',
        'Guinea',
        'Guinea-Bissau', 'Guyana', 'Haiti', 'High income countries', 'Honduras', 'Hong Kong', 'Hungary', 'Iceland',
        'India',
        'Indonesia', 'Iran', 'Iraq', 'Ireland', 'Israel', 'Italy', 'Jamaica', 'Japan', 'Jordan', 'Kazakhstan',
        'Kenya',
        'Kiribati', 'Kuwait', 'Kyrgyzstan', 'Land-locked Developing Countries (LLDC)', 'Laos',
        'Latin America and the Caribbean', 'Latvia', 'Least Developed Countries', 'Lebanon', 'Lesotho',
        'Less Developed Regions', 'Less Developed Regions, excluding China',
        'Less Developed Regions, excluding Least Developed Countries', 'Liberia', 'Libya', 'Lithuania',
        'Lower-middle-income countries', 'Low-income countries', 'Luxembourg', 'Macao', 'Madagascar', 'Malawi',
        'Malaysia',
        'Maldives', 'Mali', 'Malta', 'Martinique', 'Mauritania', 'Mauritius', 'Mayotte', 'Melanesia', 'Mexico',
        'Micronesia (country)', 'Middle Africa', 'Middle-income countries', 'Moldova', 'Mongolia', 'Montenegro',
        'More Developed Regions', 'Morocco', 'Mozambique', 'Myanmar', 'Namibia', 'Nepal', 'Netherlands',
        'New Caledonia',
        'New Zealand', 'Nicaragua', 'Niger', 'Nigeria', 'No income group available', 'North Korea',
        'North Macedonia',
        'Northern Africa', 'Northern Africa and Western Asia', 'Northern America', 'Northern Europe', 'Norway',
        'Oceania',
        'Oceania (excluding Australia and New Zealand)', 'Oman', 'Pakistan', 'Palestine', 'Panama',
        'Papua New Guinea',
        'Paraguay', 'Peru', 'Philippines', 'Poland', 'Portugal', 'Puerto Rico', 'Qatar', 'Reunion', 'Romania',
        'Russia',
        'Rwanda', 'Saint Lucia', 'Saint Vincent and the Grenadines', 'Samoa', 'Sao Tome and Principe',
        'Saudi Arabia',
        'Senegal', 'Serbia', 'Seychelles', 'Sierra Leone', 'Singapore', 'Slovakia', 'Slovenia',
        'Small Island Developing States (SIDS)', 'Solomon Islands', 'Somalia', 'South Africa', 'South America',
        'South Eastern Asia', 'South Korea', 'South Sudan', 'Southern Africa', 'Southern Asia', 'Southern Europe',
        'Spain',
        'Sri Lanka', 'Sub-Saharan Africa', 'Sudan', 'Suriname', 'Sweden', 'Switzerland', 'Syria', 'Taiwan',
        'Tajikistan',
        'Tanzania', 'Thailand', 'Timor', 'Togo', 'Tonga', 'Trinidad and Tobago', 'Tunisia', 'Turkey',
        'Turkmenistan',
        'Uganda', 'Ukraine', 'United Arab Emirates', 'United Kingdom', 'United States',
        'United States Virgin Islands',
        'Upper-middle-income countries', 'Uruguay', 'Uzbekistan', 'Vanuatu', 'Venezuela', 'Vietnam',
        'Western Africa',
        'Western Asia', 'Western Sahara', 'World', 'Yemen', 'Zambia', 'Zimbabwe')

    lblselectsountry1 = Label(root, text="Select country :").grid(row=0, column=0, pady=15)
    n1 = StringVar()
    countries_list1 = Combobox(root, width=27, textvariable=n1, values=country_names)
    countries_list1.grid(row=0, column=1)

    lblselectsountry2 = Label(root, text="Select country :").grid(row=1, column=0, pady=15)
    n2 = StringVar()
    countries_list2 = Combobox(root, width=27, textvariable=n2, values=country_names)
    countries_list2.grid(row=1, column=1)

    btnAddCountry = Button(root, text='Add Country', command=add_country).grid(row=0, column=4)
    btnSubmit = Button(root, text='Submit', command=submit_click).grid(row=0, column=6)
    
    
    root.mainloop()