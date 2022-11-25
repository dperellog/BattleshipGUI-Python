#!/usr/bin/env python
# -*- coding: utf-8 -*-

#=== IMPORTS ===#
from tkinter import *
from tkinter import ttk
import os
#Importar les classes i el diccionari de llenguatges.
from classes import *
import languages as get

class Battleship(object):
    #=== CONSTANTS ===#
    MIDATAULELL = 10
    FLOTA = [{'nom':'fleet/four','mida':4,'quantitat':1},
            {'nom':'fleet/three','mida':3,'quantitat':2},
            {'nom':'fleet/two','mida':2,'quantitat':3},
            {'nom':'fleet/one','mida':1,'quantitat':4}]
    VIDES = 50
    LLENGUATGES = ('ca', 'es', 'en')

    idioma = 'ca'
    jocsActius = []
    taulerActual = 0
    
    def __init__(self):

        #Iniciar finestra principal:
        self.arrel = Tk()
        self.arrel.title("Battleship - David Perelló")
        self.arrel.geometry("200x350")
        self.arrel.resizable(0,0)

        self.menuPrincipal = ttk.Frame(self.arrel, padding=(10, 10))
        self.menuPrincipal.pack(side=TOP)
        self.imgVaixell = PhotoImage(file=f'{os.getcwd()}\imgs\mainimg.png')      

        self.mostraMenu()

        self.arrel.mainloop()

    def mostraMenu(self):
        #Muntar els windgets del menú principal:      
        self.mainimg = ttk.Label(self.menuPrincipal, image=self.imgVaixell, 
                                 anchor="center")
        self.mainimg.pack(side=TOP, fill=BOTH, expand=True, 
                          padx=10, pady=5)

        self.botoNovaPartida= ttk.Button(self.menuPrincipal, text=get.text('menu/newGame', self.idioma), padding=(5,5), command=self.finestraFormulariNouTauler).pack(side=TOP, expand=YES, pady=10)
        self.botoRecuperarPartida= ttk.Button(self.menuPrincipal, text=get.text('menu/resumeGame', self.idioma), padding=(5,5), command=self.recuperarPartida).pack(side=TOP, expand=YES, pady=10)
        
        self.botoIdioma= ttk.Button(self.menuPrincipal, text=get.text('menu/changeLng', self.idioma), command=self.cambiarIdiomaFinestra).pack(side=TOP, expand=YES, pady=10)
        self.botoSortir= ttk.Button(self.menuPrincipal, text=get.text('menu/exitGame', self.idioma), command=quit).pack(side=TOP, expand=YES, pady=10)

    def cambiarIdiomaFinestra(self):
        self.finestraIdioma = Toplevel(self.arrel)
        self.finestraIdioma.title("Language")

        caBtn = ttk.Button(self.finestraIdioma, text="Català", command=lambda : self.cambiarIdioma('ca')).pack(side=TOP, expand=YES, pady=10)
        esBtn = ttk.Button(self.finestraIdioma, text="Español", command=lambda : self.cambiarIdioma('es')).pack(side=TOP, expand=YES, pady=10)
        enBtn = ttk.Button(self.finestraIdioma, text="English", command=lambda : self.cambiarIdioma('en')).pack(side=TOP, expand=YES, pady=10)

        self.finestraIdioma.focus()
        self.finestraIdioma.grab_set()

    def cambiarIdioma(self, idioma):
        self.idioma = idioma
        self.finestraIdioma.destroy()

        #Destruir el conteingut actual del menu:
        for boto in self.menuPrincipal.winfo_children():
            boto.destroy()

        self.mostraMenu()
        
    def recuperarPartida(self):
        self.finestraCambiarPartida = Toplevel(self.arrel)
        self.finestraCambiarPartida.title(get.text('menu/resumeGame', self.idioma))
        self.finestraCambiarPartida.focus()
        self.finestraCambiarPartida.grab_set()

        titolFinestra = ttk.Label(self.finestraCambiarPartida, text=get.text('menu/activePlaygrounds', self.idioma))
        titolFinestra.pack(side=TOP, pady= 10)

        if len(self.jocsActius) > 0:
            for partida in self.jocsActius:
                botoTaulell = ttk.Button(self.finestraCambiarPartida, text=partida.getName(), padding=(5,5), command=lambda tauler=partida : self.actualitzaTaulerActual(tauler))
                botoTaulell.pack(side=TOP)
        else:
            noActiveGames = Label(self.finestraCambiarPartida, text=get.text('errors/noActiveGames', self.idioma), foreground='red')
            noActiveGames.pack(side=TOP, pady=10, padx=5)


    def obrirFinestraTauler(self):
        self.finestraTauler = Toplevel(self.arrel)
        self.finestraTauler.title(get.text("playground/name", self.idioma, self.taulerActual.getName()))

        #Tauler (botons):
        self.taulerFrame = ttk.Frame(self.finestraTauler, padding=(10, 10))
        self.taulerFrame.grid(row=0, column=0)

        #Tauler (info):
        self.taulerFrameInfo = ttk.Frame(self.finestraTauler, padding=(10, 10))
        self.taulerFrameInfo.grid(row=0, column=1)

        #Tauler info - nom.
        info = ttk.Label(self.taulerFrameInfo, text=get.text('playground/info', self.idioma),font=('Arial 20'))
        taulerNom = ttk.Label(self.taulerFrameInfo, text=get.text('playground/name', self.idioma, self.taulerActual.getName()),font=('Arial 15'))
        info.pack(side=TOP)
        taulerNom.pack(side=TOP)

        #Tauler info - vides.
        if self.taulerActual.videsActivades:
            self.taulerVidesInfo = ttk.Frame(self.taulerFrameInfo, padding=(10, 10))
            self.taulerVidesInfo.pack(side=TOP)

            self.videsFeedback = IntVar(self.taulerVidesInfo, self.taulerActual.getVides())

            videsTitle = ttk.Label(self.taulerVidesInfo, text=get.text('playground/remaining', self.idioma), font=('Arial 15'))
            vides = ttk.Label(self.taulerVidesInfo, textvariable=self.videsFeedback, font=('Arial 20'))
            videsTitle.pack(side=TOP)
            vides.pack(side=TOP)

        #Tauler info - borrar tauler.
        delBtn = ttk.Button(self.taulerFrameInfo, text=get.text('playground/delete', self.idioma), command=self.borrarTauler)
        delBtn.pack(side=BOTTOM, pady=10)

        #Tauler info - feedback.
        self.taulerFeedback = StringVar()
        self.taulerResponseInfo = Entry(self.finestraTauler, textvariable=self.taulerFeedback,
        borderwidth=1, justify=CENTER, font=('Arial 18'), width=50)

        self.taulerResponseInfo.grid(row=1, column=0)


        self.refrescaTauler()
            
        self.finestraTauler.focus()
        self.finestraTauler.grab_set()

    def refrescaTauler(self):
        #Destruir el conteingut actual del frame:
        for boto in self.taulerFrame.winfo_children():
            boto.destroy()

        #Generar el taulell:
        for i in range(9):
            for j in range(9):
                objecteCasella = self.taulerActual.getCasella((i,j))
                if objecteCasella.visible:
                    self.casella = ttk.Button(self.taulerFrame, state='disabled', text=str(objecteCasella), padding=(5,5), command=lambda i=i, j=j: self.tret((i,j)))
                else:
                    self.casella = ttk.Button(self.taulerFrame, text=str(objecteCasella), padding=(5,5), command=lambda i=i, j=j: self.tret((i,j)))
                self.casella.grid(column=j, row=i)

        if self.taulerActual.videsActivades:
            self.videsFeedback.set(self.taulerActual.getVides())

    def finestraFormulariNouTauler(self):
        #Formulari del tauler:

        self.formulariNouTauler = Toplevel(self.arrel)
        self.formulariNouTauler.title(get.text('menu/createNewGame', self.idioma))
        self.formulariNouTauler.focus()
        self.formulariNouTauler.grab_set()

        self.nomTauler = StringVar()
        self.videsActivades = BooleanVar()

        textNomTauler = ttk.Label(self.formulariNouTauler, text=get.text('playground/enterName', self.idioma))
        textNomTauler.pack(side=TOP, pady=10, padx=5)

        nomTauler = ttk.Entry(self.formulariNouTauler, textvariable=self.nomTauler, width=30)
        nomTauler.pack(side=TOP, pady=10, padx=5)

        vides = ttk.Checkbutton(self.formulariNouTauler, text=get.text('playground/playWLives', self.idioma), variable=self.videsActivades)
        vides.pack(side=TOP, pady=10)

        crearTaulerBtn = ttk.Button(self.formulariNouTauler, text=get.text('menu/createNewGame', self.idioma), command=lambda : self.nouTauler(self.nomTauler.get()))
        crearTaulerBtn.pack(side=TOP, pady=10)


    def nouTauler(self, nomTauler):
        self.formulariNouTauler.destroy()
        #Inicialitzar el taulell.
        tauler = Tauler(self.MIDATAULELL,self.FLOTA,nomTauler,self.VIDES if self.videsActivades.get() else 0, self.idioma)

        self.jocsActius.append(tauler)
        self.taulerActual = tauler
        self.obrirFinestraTauler()

    def actualitzaTaulerActual(self, tauler):
        self.taulerActual = tauler
        self.finestraCambiarPartida.destroy()
        self.obrirFinestraTauler()

    def tret(self, coords):
        self.taulerFeedback.set(self.taulerActual.tret(coords))
        self.refrescaTauler()

    def borrarTauler(self):
        #Eliminar de la llista de jocs actius:
        for i in range(len(self.jocsActius)):
            if self.jocsActius[i].getID() == self.taulerActual.getID():
                del self.jocsActius[i]
                break

        self.finestraTauler.destroy()


Battleship()