from tkinter import*
import requests
import webbrowser

def update():
    global label, lat, long, url, label1
    url="http://api.open-notify.org/iss-now.json"
    result=requests.get(url)
    result=result.json()
    pos=result['iss_position']
    long=pos['longitude']
    lat=pos['latitude']
    label['text']=f'Долгота: {long}\nШирота: {lat}'

    responce=requests.get("http://api.open-notify.org/astros.json")
    responce=responce.json()
    txt=responce['people']
    s='Сколько людей сейчас в космосе: '+str(responce['number'])+'\n'+'\n'
    for i in txt:
        s+=i['name']
        s+='\n'
    label1['text']=s
            

def click():
    global long, lat
    url=f'https://www.google.com/maps/place/{lat},{long}'
    webbrowser.open(url)

url="http://api.open-notify.org/iss-now.json"
result=requests.get(url)
result=result.json()
pos=result['iss_position']
long=pos['longitude']
lat=pos['latitude']

a=Tk()
a.iconbitmap('images/icon.ico')
a.title('МКС online')
a.resizable(width=False,height=False)

label=Label(text=f'Долгота: {long}\nШирота: {lat}',
            font=('Arial','12','bold'),fg='red')
label.pack()

responce=requests.get("http://api.open-notify.org/astros.json")
responce=responce.json()
txt=responce['people']
s='Сколько людей сейчас в космосе: '+str(responce['number'])+'\n'+'\n'
for i in txt:
    s+=i['name']
    s+='\n'
label1=Label(text=s,font=('Times New Roman','12'))
label1.pack(pady=3)

btn=Button(text='посмотреть на google maps',command=click,
           font='Arial 9')
btn.pack(pady=4)

ubtn=Button(text='Обновить',command=update,
           font=('Arial','9','bold'),cursor='watch')
ubtn.pack(pady=4)

a.mainloop()

