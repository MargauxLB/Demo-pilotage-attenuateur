
from tkinter import *
import Attenuateur


def send_value():
    att=Attenuateur.Attenuateur()
    if len(valuentry.get()) ==0:
        return


    port=comentry.get()
    ip=ipentry.get()

    try:
        value = float(valuentry.get())
        if len(port) != 0:
            att.connexion_serial(port)

        if len(ip) != 0:
            att.connexion_network(ip)

        att.set_value(value)
    except Attenuateur.AttenuateurSerialException:
        erreur.config(text='Serial port error')
    except Attenuateur.AttenuateurNetworkException:
        erreur.config(text='Network error')
    except ValueError:
        erreur.config(text='Value error')
    except:
        erreur.config(text='Unknown error')
    else:
        erreur.config(text='Ok')


    att.close()


app = Tk()

app.geometry('200x200+800+300')
app.title('ATT HYTEM controler')
connexiontype=IntVar()

Label(app, text='ComPort : ').grid(row=1, column=1)
comentry=Entry(app)
comentry.grid(row =1,column=2)
Label(app, text='IP : ').grid(row=2, column=1)
ipentry=Entry(app)
ipentry.grid(row =2,column=2)
Label(app, text='Value : ').grid(row=3, column=1)
valuentry=Entry(app)
valuentry.grid(row =3,column=2)
Button(text='Send', command=send_value).grid(row=4, columnspan=3)
erreur = Label(app, font=('Arial',15))
erreur.grid(row=5, columnspan=3 )



app.mainloop()