from tkinter import *
import mysql.connector as mysql
import tkinter.messagebox as MessageBox
import pymysql


root = Tk()
root.geometry("600x300")
root.title("CRUD avec Tkinter et MySQL")



def inserer():
    id = e_id.get()
    name = e_name.get()
    numero = e_numero.get()

    if(id=="" or name=="" or numero=="" ):
       MessageBox.showinfo("Echec", "Tous les champs sont requis")
    else:
        con = pymysql.connect(host="localhost", user="root", password="", database="formation")
        cursor = con.cursor()
        cursor.execute("insert into odc values('"+ id +"','"+name+"','"+numero+"')")
        cursor.execute("commit")
        MessageBox.showinfo("inserer status", "Insertion successfully")
        con.close()

"""def supprimer():


    if(e_id.get()==""):

       MessageBox.showinfo("Echec", "id est requis")
    else:
        con = mysql.connect(host ="localhost", user="root", password="", database="python")
        custor = con.cursor()
        custor.excute("inserer into student values('"+ id +"','"+name+"','"+numero+"')")
        cursor.excute("commit");
        MessageBox.showinfo("Suppression", "Delete successfully");
        con.close();

def modifier():
    id = e_id.get()
    name = e_name.get();
    numero = e_numero.get();

    if(id=="" or name=="" or numero=="" ):

       MessageBox.showinfo("Echec", "Tous les champs sont requis")
    else:
        con = mysql.connect(host ="localhost", user="root", password="", database="python")
        custor = con.cursor()
        custor.excute("inserer into student values('"+ id +"','"+name+"','"+numero+"')")
        cursor.excute("commit");

        e_id.supprimer(0, "end")
        e_name.supprimer(0, "end")
        e_numero.supprimer(0, "end")
        MessageBox.showinfo("inserer status", "Insertion successfully");
        con.close();"""

"""def afficher():
    id = e_id.get()
    name = e_name.get();
    numero = e_numero.get();

    if(id=="" or name=="" or numero=="" ):

       MessageBox.showinfo("inserer status", "All Field are required")
    else:
        con = mysql.connect(host ="localhost", user="root", password="", database="python")
        custor = con.cursor()
        custor.excute("inserer into student values('"+ id +"','"+name+"','"+numero+"')")
        cursor.excute("commit");
        MessageBox.showinfo("inserer status", "Insertion successfully");
        con.close();"""



id = Label(root, text="Entrer ID")
id.place(x=30, y=30)
name = Label(root, text="Entrer Nom")
name.place(x=30, y=60)
numero = Label(root, text="Entrer Numéro")
numero.place(x=30, y=90)

e_id = Entry()
e_id.place(x=150, y=30)



e_name = Entry()
e_name.place(x=150, y=60)

e_numero = Entry()
e_numero.place(x=150, y=90)

inserer = Button(root, text="Insérer", command=inserer)
inserer.place(x=30, y=140)

supprimer = Button(root, text="Supprimer", command=quit)
supprimer.place(x=100, y=140)

modifier = Button(root, text="Modifier", command=quit)
modifier.place(x=200, y=140)

afficher = Button(root, text="Afficher", command=quit)
afficher.place(x=300, y=140)

list = Listbox(root)
list.place(x=420, y=30)

root.mainloop()





