# -*- coding: utf-8 -*
#Installation du module xlutils
#pip install xlutils
import numpy as np
import xlrd
import datetime
import os, glob, platform,pdb, shutil

Mois=['Janvier','Fevrier','Mars','Avril','Mai','Juin','Juillet','Aout','Septembre','Octobre','Novembre','Décembre']

#RAZ du fichier log
f=open('log.txt','w')

path=r"../Informatique/progression_2021_2022_Info_MPSI.xls"#chemin de la progression
path_classe=''
path_site='pdf'#Chemin pour exporter les pdf vers site
path_site_ds='/Users/emiliendurif/Dropbox/cpge/ipt_mpsi_ds'#Chemin pour exporter les pdf vers site


# os.chdir(os.system('pwd'))

#Separateur de dossier
if platform.system()=='Windows':
    sep='\\'
    path_ref=os.popen('cd').readlines()[0].strip()
    copy='copy '
    rm='DEL '
    cmd_latex='pdflatex '
else:
    sep='/'
    path_ref=os.popen('pwd').readlines()[0].strip()
    copy='cp '
    rm='rm '
    cmd_latex='/usr/local/texlive/2017/bin/x86_64-darwin/pdflatex '

####
#Definition des colonnes dans le tableau excel
####


def convdate(date0):
    d0=datetime.date(1900,1,1)
    date=d0+datetime.timedelta(days=(date0-2))
    date=str(date.day)+' '+Mois[date.month-1]+' '+str(date.year)
    return date



    


def lire_semanier(path):
    """a partir d'une feuille excel correspondant au sémanier de la progression renvoie deux listes de tuple donnant des infos sur les cours et td : (date,cycle,numero,nom du cycle,nom du document, supports d'application pour le cours)"""
    #Ouverture de la progression excel
    classeur=xlrd.open_workbook(path)
    feuilles=classeur.sheet_names()
    
    #Ouverture de la feuille du semanier
    d0=datetime.date(1900,1,1)
    for f in feuilles:
        if "Semanier" in f:
            fs=classeur.sheet_by_name(f)
    col_date,col_num_cycle,col_name_cycle,col_num_cours,col_num_tp,col_name_cours,col_name_tp,col_supports_TD,col_supports_tp,col_competences_cours,col_competences_tp,col_figures,col_ref_cours\
    =1,2,3,4,6,5,7,10,10,11,12,15,16
    nligne=40#Derniere ligne où figure une donnée
    delta_td=1#position du jour des TD dans la semaine
    delta_cours=2#position du jour des cours dans la semaine
    delta_tp=3#position du jour des TP dans la semaine
    liste_cours=[]
    liste_cycle=[]
    liste_tp=[]
    info_cours=[]
    info_tp=[]
    for k in range(1,nligne):
    #for k in range(1,2):
        if 'Vacances' not in str(fs.cell_value(k,0)):
            delta = datetime.timedelta(days=(fs.cell_value(k,col_date)-2))
            d_s=d0+delta#Date du début de la semaine
            d_cours=d_s+datetime.timedelta(delta_cours)#Date du cours
            d_td=d_s+datetime.timedelta(delta_td)#Date du TD
            d_tp=d_s+datetime.timedelta(delta_tp)#Date du TD
            if fs.cell_value(k,col_num_cours)!='':
                num_cours=int(fs.cell_value(k,col_num_cours)) #Numero du chapitre
            else:
                num_cours=0
            if num_cours<10:
                num_cours='0'+str(num_cours)
            else:
                num_cours=str(num_cours)
            n_tp=int(fs.cell_value(k,col_num_tp)) #Numero du TP
            if fs.cell_value(k,col_num_cycle)!='':
                n_cycle=int(fs.cell_value(k,col_num_cycle))#numero du cycle
                name_cycle=fs.cell_value(k,col_name_cycle)#nom du cycle
                liste_cycle.append(n_cycle)
            else:
                n_cycle=liste_cycle[-1]
                # name_cycle=liste_name_cycle[-1]
            n_cours='C'+str(n_cycle)+'-'+str(num_cours)#numero du cours Ci-j avec i le cycle et j le chapitre
            # #Gestion des cours
            if n_cours not in liste_cours:
                name_cours=fs.cell_value(k,col_name_cours)
                liste_cours.append(n_cours)
                supports=fs.cell_value(k,col_supports_TD)
                competences=fs.cell_value(k,col_competences_cours)
                figures=fs.cell_value(k,col_figures)
                date_cours=str(d_cours.day)+' '+Mois[d_cours.month-1]+' '+str(d_cours.year)
                ref_cours=str(n_cycle)+'-'+str(num_cours)
                info_cours.append((date_cours,n_cycle,num_cours,name_cycle,name_cours,supports,competences,figures,ref_cours))
            # #Gestion des TP
            if n_tp not in liste_tp:
                name_tp=fs.cell_value(k,col_name_tp)
                num_tp=int(fs.cell_value(k,col_num_tp))
                if num_tp<10:
                    num_tp='0'+str(num_tp)
                else:
                    num_tp=str(num_tp)
                supports=fs.cell_value(k,col_supports_tp)
                competences=fs.cell_value(k,col_competences_tp)
                figures=fs.cell_value(k,col_figures)
                liste_tp.append(n_tp)
                ref_cours=fs.cell_value(k,col_ref_cours)#Reference du cours correspondant
                date_tp=str(d_tp.day)+' '+Mois[d_tp.month-1]+' '+str(d_tp.year)
                info_tp.append((date_tp,n_cycle,num_tp,name_cycle,name_tp,supports,competences,figures,ref_cours))
    return info_tp,info_cours
            


    
def trouver_repertoire(info_activite):
    """Renvoie le repertoire dans lequel ecrire les infos de l'activité"""
    (date,n_cycle,num_activite,name_cycle,name_activite,supports,competences,figures,ref_cours)=info_activite
    n_cycle,num_activite=ref_cours.split(';')[0].split('-')
    if int(num_activite)<10 and len(num_activite)<2:
        num_activite='0'+str(num_activite)
    for r in os.listdir():
        if 'Cy_0'+str(n_cycle) in r and '.pdf' not in r:
            rep_cycle=r
            for r1 in os.listdir(rep_cycle+'/'):
                if 'Ch_'+str(num_activite) in r1:
                    rep_chapitre=r1
    rep=rep_cycle+sep+rep_chapitre
    return rep
    
def genere_fichiers_tex0(info_activite,type_activite):
    '''Genere le fichier .tex à partir de l'activite donne et du bon repertoire'''
    if type_activite=='ds':
        (num_ds_str,titre,supports,chapitres,cycles,date_ds)=ds
        rep='DS/DS'+num_ds_str
    else:
        (date,n_cycle,num_activite,name_cycle,name_activite,supports,competences,figures,ref_cours)=info_activite
        rep=trouver_repertoire(info_activite)
        if int(num_activite)<10 and len(num_activite)<2:
            num_activite='0'+num_activite
    if type_activite=='cours':
        os.system(copy+'style'+sep+'Cy_i_Ch_j_Cours.tex '+rep+sep+'Cy_0'+str(n_cycle)+'_Ch_'+str(num_activite)+'_Cours.tex')
        os.system(copy+'style'+sep+'Cy_i_Ch_j_Cours_PDF.tex '+rep+sep+'Cy_0'+str(n_cycle)+'_Ch_'+str(num_activite)+'_Cours_PDF.tex')
        os.system(copy+'style'+sep+'Cy_i_livret_Ch_j.tex '+rep+sep+'Cy_0'+str(n_cycle)+'_livret_Ch_'+str(num_activite)+'.tex')
        os.system(copy+'style'+sep+'Cy_i_Ch_j_TD_j.tex '+rep+sep+'Cy_0'+str(n_cycle)+'_Ch_'+str(num_activite)+'_TD_'+str(num_activite)+'.tex')
        os.system(copy+'style'+sep+'Cy_i_Ch_j_TD_k_cor_pdf.tex '+rep+sep+'Cy_0'+str(n_cycle)+'_Ch_'+str(num_activite)+'_TD_'+str(num_activite)+'_cor_pdf.tex')
        os.system(copy+'style'+sep+'Cy_i_Ch_j_TD_j_cor.tex '+rep+sep+'Cy_0'+str(n_cycle)+'_Ch_'+str(num_activite)+'_TD_'+str(num_activite)+'_cor.tex')
        # print(rep+sep+'Cy_0'+str(n_cycle)+'_Ch_0'+str(num_activite)+'_Cours_PDF.tex')
        changer_ligne(rep+sep+'Cy_0'+str(n_cycle)+'_Ch_'+str(num_activite)+'_Cours_PDF.tex','\\input{Cy_01_Ch_01_Cours.tex}','\\input{Cy_0'+str(n_cycle)+'_Ch_'+str(num_activite)+'_Cours.tex}')
        changer_ligne(rep+sep+'Cy_0'+str(n_cycle)+'_livret_Ch_'+str(num_activite)+'.tex','\\input{Cy_01_Ch_01_Cours.tex}','\\input{Cy_0'+str(n_cycle)+'_Ch_'+str(num_activite)+'_Cours.tex}')
        changer_ligne(rep+sep+'Cy_0'+str(n_cycle)+'_livret_Ch_'+str(num_activite)+'.tex','\\input{Cy_01_Ch_01_TD_01.tex}','\\input{Cy_0'+str(n_cycle)+'_Ch_'+str(num_activite)+'_TD_'+str(num_activite)+'.tex}')
        changer_ligne(rep+sep+'Cy_0'+str(n_cycle)+'_Ch_'+str(num_activite)+'_TD_'+str(num_activite)+'_cor_pdf.tex','\\input{Cy_02_Ch_01_TD_01}','\\input{Cy_0'+str(n_cycle)+'_Ch_'+str(num_activite)+'_TD_'+str(num_activite)+'_cor.tex}')
    elif type_activite=='tp':
        num_chapitre=ref_cours.split(';')[0].split('-')[1]
        if int(num_chapitre)<10 and len(num_chapitre)<2:
            num_chapitre='0'+num_chapitre
        if os.path.exists(rep+sep+'Cy_0'+str(n_cycle)+'_Ch_'+str(num_chapitre)+'_TP_'+num_activite)==False:
            os.mkdir(rep+sep+'Cy_0'+str(n_cycle)+'_Ch_'+str(num_chapitre)+'_TP_'+num_activite)
            #TP : enonce
        os.system(copy+'style'+sep+'Cy_i_Ch_j_TP_k.tex '+rep+'/Cy_0'+str(n_cycle)+'_Ch_'+str(num_chapitre)+'_TP_'+num_activite+sep+'Cy_0'+str(n_cycle)+'_Ch_'+str(num_chapitre)+'_TP_'+num_activite+'.tex')
        os.system(copy+'style'+sep+'Cy_i_Ch_j_TP_k_pdf.tex '+rep+sep+'Cy_0'+str(n_cycle)+'_Ch_'+str(num_chapitre)+'_TP_'+num_activite+sep+'Cy_0'+str(n_cycle)+'_Ch_'+str(num_chapitre)+'_TP_'+num_activite+'_pdf.tex')
        changer_ligne(rep+sep+'Cy_0'+str(n_cycle)+'_Ch_'+str(num_chapitre)+'_TP_'+num_activite+sep+'Cy_0'+str(n_cycle)+'_Ch_'+str(num_chapitre)+'_TP_'+num_activite+'_pdf.tex','\\input{Cy_01_Ch_01_TP_01}','\\input{Cy_0'+str(n_cycle)+'_Ch_'+str(num_chapitre)+'_TP_'+num_activite+'.tex}')
            #TP : corrige
        os.system(copy+'style'+sep+'Cy_i_Ch_j_TP_k.tex '+rep+'/Cy_0'+str(n_cycle)+'_Ch_'+str(num_chapitre)+'_TP_'+num_activite+sep+'Cy_0'+str(n_cycle)+'_Ch_'+str(num_chapitre)+'_TP_'+num_activite+'-cor.tex')
        os.system(copy+'style'+sep+'Cy_i_Ch_j_TP_k_pdf.tex '+rep+sep+'Cy_0'+str(n_cycle)+'_Ch_'+str(num_chapitre)+'_TP_'+num_activite+sep+'Cy_0'+str(n_cycle)+'_Ch_'+str(num_chapitre)+'_TP_'+num_activite+'_pdf-cor.tex')
        changer_ligne(rep+sep+'Cy_0'+str(n_cycle)+'_Ch_'+str(num_chapitre)+'_TP_'+num_activite+sep+'Cy_0'+str(n_cycle)+'_Ch_'+str(num_chapitre)+'_TP_'+num_activite+'_pdf-cor.tex','\\input{Cy_01_Ch_01_TP_01}','\\input{Cy_0'+str(n_cycle)+'_Ch_'+str(num_chapitre)+'_TP_'+num_activite+'-cor.tex}')
        changer_ligne(rep+sep+'Cy_0'+str(n_cycle)+'_Ch_'+str(num_chapitre)+'_TP_'+num_activite+sep+'Cy_0'+str(n_cycle)+'_Ch_'+str(num_chapitre)+'_TP_'+num_activite+'-cor.tex','\\input{tp.tex}','\\input{tp-cor.tex}')
        changer_ligne(rep+sep+'Cy_0'+str(n_cycle)+'_Ch_'+str(num_chapitre)+'_TP_'+num_activite+sep+'Cy_0'+str(n_cycle)+'_Ch_'+str(num_chapitre)+'_TP_'+num_activite+'_pdf-cor.tex','\\corrigefalse','\\corrigetrue')
        #DS
    elif type_activite=='ds':
        os.system(copy+'style'+sep+'DSk.tex '+rep+sep+'DS'+num_ds_str+'.tex')
        os.system(copy+'style'+sep+'DSk_pdf.tex '+rep+sep+'DS'+num_ds_str+'_pdf.tex')
        changer_ligne(rep+sep+'DS'+num_ds_str+'_pdf.tex','\\input{Cy_01_Ch_01_TP_01}','\\input{DS'+num_ds_str+'.tex}')
            #DS : corrige
        os.system(copy+'style'+sep+'DSk.tex '+rep+sep+'DS'+num_ds_str+'-cor.tex')
        os.system(copy+'style'+sep+'DSk_pdf.tex '+rep+sep+'DS'+num_ds_str+'_pdf-cor.tex')
        changer_ligne(rep+sep+'DS'+num_ds_str+'_pdf-cor.tex','\\input{Cy_01_Ch_01_TP_01}','\\input{DS'+num_ds_str+'-cor.tex}')
        changer_ligne(rep+sep+'DS'+num_ds_str+'_pdf-cor.tex','\\corrigefalse','\\corrigetrue')
        changer_ligne(rep+sep+'DS'+num_ds_str+'-cor.tex','\\input{ds.tex}','\\input{ds-cor.tex}')
        # changer_ligne(rep+sep+'Cy_0'+str(n_cycle)+'_Ch_'+str(num_chapitre)+'_TP_'+num_activite+sep+'Cy_0'+str(n_cycle)+'_Ch_'+str(num_chapitre)+'_TP_'+num_activite+'-cor.tex','\\input{tp.tex}','\\input{tp-cor.tex}')
        # changer_ligne(rep+sep+'Cy_0'+str(n_cycle)+'_Ch_'+str(num_chapitre)+'_TP_'+num_activite+sep+'Cy_0'+str(n_cycle)+'_Ch_'+str(num_chapitre)+'_TP_'+num_activite+'_pdf-cor.tex','\\corrigefalse','\\corrigetrue')
        
        
def genere_fichiers_tex(info_activite,type_activite,rep):
    '''Genere le fichier .tex à partir de l'activite donne et du bon repertoire'''
    if type_activite=='ds':
        (num_ds_str,titre,supports,chapitres,cycles,date_ds)=ds
        rep='DS/DS'+num_ds_str
    else:
        (date,n_cycle,num_activite,name_cycle,name_activite,supports,competences,figures,ref_cours)=info_activite
        if int(num_activite)<10 and len(num_activite)<2:
            num_activite='0'+num_activite
    if type_activite=='cours':
        os.system(copy+'style'+sep+'Cy_i_Ch_j_Cours.tex '+rep+sep+'Cy_0'+str(n_cycle)+'_Ch_'+str(num_activite)+'_Cours.tex')
        os.system(copy+'style'+sep+'Cy_i_Ch_j_Cours_PDF.tex '+rep+sep+'Cy_0'+str(n_cycle)+'_Ch_'+str(num_activite)+'_Cours_PDF.tex')
        os.system(copy+'style'+sep+'Cy_i_livret_Ch_j.tex '+rep+sep+'Cy_0'+str(n_cycle)+'_livret_Ch_'+str(num_activite)+'.tex')
        os.system(copy+'style'+sep+'Cy_i_Ch_j_TD_j.tex '+rep+sep+'Cy_0'+str(n_cycle)+'_Ch_'+str(num_activite)+'_TD_'+str(num_activite)+'.tex')
        os.system(copy+'style'+sep+'Cy_i_Ch_j_TD_k_cor_pdf.tex '+rep+sep+'Cy_0'+str(n_cycle)+'_Ch_'+str(num_activite)+'_TD_'+str(num_activite)+'_cor_pdf.tex')
        os.system(copy+'style'+sep+'Cy_i_Ch_j_TD_j_cor.tex '+rep+sep+'Cy_0'+str(n_cycle)+'_Ch_'+str(num_activite)+'_TD_'+str(num_activite)+'_cor.tex')
        # print(rep+sep+'Cy_0'+str(n_cycle)+'_Ch_0'+str(num_activite)+'_Cours_PDF.tex')
        changer_ligne(rep+sep+'Cy_0'+str(n_cycle)+'_Ch_'+str(num_activite)+'_Cours_PDF.tex','\\input{Cy_01_Ch_01_Cours.tex}','\\input{Cy_0'+str(n_cycle)+'_Ch_'+str(num_activite)+'_Cours.tex}')
        changer_ligne(rep+sep+'Cy_0'+str(n_cycle)+'_livret_Ch_'+str(num_activite)+'.tex','\\input{Cy_01_Ch_01_Cours.tex}','\\input{Cy_0'+str(n_cycle)+'_Ch_'+str(num_activite)+'_Cours.tex}')
        changer_ligne(rep+sep+'Cy_0'+str(n_cycle)+'_livret_Ch_'+str(num_activite)+'.tex','\\input{Cy_01_Ch_01_TD_01.tex}','\\input{Cy_0'+str(n_cycle)+'_Ch_'+str(num_activite)+'_TD_'+str(num_activite)+'.tex}')
        changer_ligne(rep+sep+'Cy_0'+str(n_cycle)+'_Ch_'+str(num_activite)+'_TD_'+str(num_activite)+'_cor_pdf.tex','\\input{Cy_02_Ch_01_TD_01}','\\input{Cy_0'+str(n_cycle)+'_Ch_'+str(num_activite)+'_TD_'+str(num_activite)+'_cor.tex}')
    elif type_activite=='tp':
            #TP : enonce
        os.system(copy+'..'+sep+'Style'+sep+'Cy_i_Ch_j_TP_k.tex '+rep+'TP'+str(num_activite)+'.tex')
        os.system(copy+'..'+sep+'Style'+sep+'Cy_i_Ch_j_TP_k_pdf.tex '+rep+'TP'+str(num_activite)+'_pdf.tex')
        changer_ligne(rep+'TP'+str(num_activite)+'_pdf.tex','\\input{Cy_01_Ch_01_TP_01}','\\input{'+'TP'+str(num_activite)+'.tex}')

            #TP : corrige
        os.system(copy+'..'+sep+'Style'+sep+'Cy_i_Ch_j_TP_k.tex '+rep+'TP'+num_activite+'-cor.tex')
        os.system(copy+'..'+sep+'Style'+sep+'Cy_i_Ch_j_TP_k_pdf.tex '+rep+sep+'TP'+num_activite+'_pdf-cor.tex')
        changer_ligne(rep+sep+'TP'+num_activite+'_pdf-cor.tex','\\input{Cy_01_Ch_01_TP_01}','\\input{TP'+num_activite+'-cor.tex}')
        changer_ligne(rep+'TP'+num_activite+'-cor.tex','\\input{tp.tex}','\\input{tp-cor.tex}')
        #changer_ligne(rep+sep+'TP_'+num_activite+'_pdf-cor.tex','\\corrigefalse','\\corrigetrue')
        #DS
    elif type_activite=='ds':
        os.system(copy+'style'+sep+'DSk.tex '+rep+sep+'DS'+num_ds_str+'.tex')
        os.system(copy+'style'+sep+'DSk_pdf.tex '+rep+sep+'DS'+num_ds_str+'_pdf.tex')
        changer_ligne(rep+sep+'DS'+num_ds_str+'_pdf.tex','\\input{Cy_01_Ch_01_TP_01}','\\input{DS'+num_ds_str+'.tex}')
            #DS : corrige
        os.system(copy+'style'+sep+'DSk.tex '+rep+sep+'DS'+num_ds_str+'-cor.tex')
        os.system(copy+'style'+sep+'DSk_pdf.tex '+rep+sep+'DS'+num_ds_str+'_pdf-cor.tex')
        changer_ligne(rep+sep+'DS'+num_ds_str+'_pdf-cor.tex','\\input{Cy_01_Ch_01_TP_01}','\\input{DS'+num_ds_str+'-cor.tex}')
        changer_ligne(rep+sep+'DS'+num_ds_str+'_pdf-cor.tex','\\corrigefalse','\\corrigetrue')
        changer_ligne(rep+sep+'DS'+num_ds_str+'-cor.tex','\\input{ds.tex}','\\input{ds-cor.tex}')
        # changer_ligne(rep+sep+'Cy_0'+str(n_cycle)+'_Ch_'+str(num_chapitre)+'_TP_'+num_activite+sep+'Cy_0'+str(n_cycle)+'_Ch_'+str(num_chapitre)+'_TP_'+num_activite+'-cor.tex','\\input{tp.tex}','\\input{tp-cor.tex}')
        # changer_ligne(rep+sep+'Cy_0'+str(n_cycle)+'_Ch_'+str(num_chapitre)+'_TP_'+num_activite+sep+'Cy_0'+str(n_cycle)+'_Ch_'+str(num_chapitre)+'_TP_'+num_activite+'_pdf-cor.tex','\\corrigefalse','\\corrigetrue')
    
def changer_ligne(fichier,ancienne_ligne,nouvelle_ligne):
    with open(fichier,'r',encoding='utf-8') as f:
        texte=f.readlines()
    with open(fichier,'w',encoding='utf-8') as f:
        for ligne in texte:
            if ancienne_ligne in ligne:
                f.write(nouvelle_ligne)
            else:
                f.write(ligne)



def trouver_chapitre(ref_cours):
    '''A partir de la reference du cours, trouve le ou les numero de chapitre et renvoie dans num_chapitre'''
    num_chapitre=ref_cours.split(';')
    if len(num_chapitre)<=1:
        num_chapitre=ref_cours.split('-')[1]
    else:
        num_chap=''
        for chap in num_chapitre:
            num_chap+=chap.split('-')[1]+' et '
        num_chapitre=num_chap[:-4]
    return num_chapitre
    
def trouve_exo_source(support):
    '''A partir d'un support renvoie le nom de l'exo et sa source'''
    classeur=xlrd.open_workbook('../Informatique/inventaire_exos.xls')
    feuilles=classeur.sheet_names()
    col_domaine,col_fichier,col_exo,col_sources=0,1,2,3
    exo,source='',''
    for f in feuilles:
        if "exos" in f:
            fs=classeur.sheet_by_name(f)
            k=1
            while fs.cell_value(k,0)!='fin':
                if fs.cell_value(k,col_domaine)+'/'+fs.cell_value(k,col_fichier)==support:
                    exo=fs.cell_value(k,col_exo)
                    source=fs.cell_value(k,col_sources)
                k+=1
    return exo,source

def genere_entete(rep,info_activite,type_activite):
    """A partir du cours dont le chemin est donne par rep la fonction genere l'entete donnant toutes infos permettant de generer l'entete du cours."""
    if type_activite=='ds':
        (num_ds_str,name_activite,supports,ref_cours,n_cycle,date)=info_activite
        num_activite=num_ds_str
        competences=''
        n_cycle=str(int(n_cycle))
        name_cycle='Cycle'+str(int(n_cycle))
        num_chapitre=trouver_chapitre(ref_cours)
        date=convdate(date)
        figures=''
    else:
        (date,n_cycle,num_activite,name_cycle,name_activite,supports,competences,figures,ref_cours)=info_activite
        n_cycle= "Semestre 1" # Mauvais HACK :) 
    #competences=competences.split(';')
        num_chapitre=trouver_chapitre(ref_cours)
    if type_activite=='cours':
        chemin_relatif='../../'
    elif type_activite=='tp':
        chemin_relatif='../../../'
    elif type_activite=='ds':
        chemin_relatif='../../'
    if type_activite=='cours':
        file_entete=rep+sep+'info_entete.tex'
        if os.path.exists(rep+sep+'cours/'):
            os.system('rm -Rf '+rep+sep+'cours/')
        if os.path.exists(rep+sep+'TD_01/'):
            os.system('rm -Rf '+rep+sep+'TD_01/')
        if os.path.exists(rep+sep+'TP_01/'):
            os.system('rm -Rf '+rep+sep+'TP_01/')
        if os.path.exists(rep+sep+'cours.tex')==False:
            os.system(copy+'style/cours0.tex '+rep+sep+'cours.tex')
        if os.path.exists(rep+sep+'td.tex')==False:
            os.system(copy+'style/td0.tex '+rep+sep+'td.tex')
        if os.path.exists(rep+sep+'images/')==False:
            os.system('mkdir '+rep+sep+'images/')
    elif type_activite=='tp':
        file_entete=rep+'info_entete.tex'
    elif type_activite=='ds':
        file_entete=rep+sep+'info_entete.tex'
    else:
        print("mauvais choix d'activite")
    with open(file_entete,'w',encoding='utf-8') as f:
        texte_entete=''
        with open('../Style'+sep+'info_Entete0.tex','r',encoding='utf-8') as f0:
            ligne=f0.readline()
            while ligne!='':
                ligne=f0.readline()
                if '\\def\\xxnumpartie' in ligne:
                    texte_entete+='\\def\\xxnumpartie{'+str(n_cycle)+'}\n'
                elif '\\def\\xxpartie' in ligne:
                    texte_entete+='\\def\\xxpartie{'+str(name_cycle)+'}\n'
                elif '\\def\\xxnomchapitre' in ligne:
                    texte_entete+='\\def\\xxnomchapitre{'+name_activite+'}\n'
                elif '\\def\\xxnumchapitre' in ligne:
                    texte_entete+='\\def\\xxnumchapitre{'+str(num_chapitre)+'}\n'
                elif '\\def\\xxnumactivite' in ligne:
                    texte_entete+='\\def\\xxnumactivite{'+str(num_activite)+'}\n'
                elif '\\def\\xxchapitre' in ligne:
                    texte_entete+='\\def\\xxchapitre{'+str(num_chapitre)+'}\n'
                elif '\\def\\xxdate' in ligne:
                    texte_entete+='\\def\\xxdate{'+date+'}\n'
                elif '\\chapterimage{' in ligne:
                    texte_entete+='\\chapterimage{'+figures+'}\n'
                elif '\\lstinputpath{}' in ligne:
                    if type_activite=='cours':
                        texte_entete+='%\\lstinputpath{}'
                    else:
                        texte_entete+='\\lstinputpath{'
                        for support in supports.split(';'):
                            if support[:1]=='F:':
                                support=support[2:]
                            texte_entete+='{'+chemin_relatif+'Informatique/exercices/'+support+'/}'
                        texte_entete+='}\n'
                elif '\\graphicspath{{../../style/png/}{images/}' in ligne:
                    texte_entete+='\\graphicspath{{'+chemin_relatif+'style/png/}{images/}'
                    for support in supports.split(';'):
                        texte_entete+='{'+chemin_relatif+'Informatique/exercices/'+support+'/}'
                    texte_entete+='}\n'
                elif '\\begin{itemize}[label=\\ding{112},font=\\color{ocre}]' in ligne:
                    texte_entete+='\\begin{itemize}[label=\\ding{112},font=\\color{ocre}]\n'
                    if competences=='':
                        texte_entete+='\\item\n'
                    else:
                        code_competence,nom_long,nom_court=trouver_texte_competence(competences,path)
                        for k in range(len(code_competence)):
                            texte_entete+='\\item '+code_competence[k]+' : '+nom_court[k]+'\n'
                elif '%Infos sur les supports' in ligne:
                    texte_entete+='%Infos sur les supports\n'
                    texte_1='\\def\\xxtitreexo{'
                    texte_2='\\def\\xxsourceexo{\\hspace{.2cm} \\footnotesize{\\textbf{Sources : }'
                    n_exo=1
                    for support in supports.split(';'):
                        exo,source=trouve_exo_source(support)
                        #texte_1+=exo+'\n'
                        if source!='':
                            texte_2+='exercice '+str(n_exo)+' : '+source+'\n'
                        else:
                            texte_2+=source+'\n'
                        n_exo+=1
                    texte_1+=name_activite+'}\n'
                    texte_2+='}}\n'
                    texte_entete+=texte_1+texte_2
                else: 
                    texte_entete+=ligne
        f.write(texte_entete)

def trouver_texte_competence(competences,path):
    '''A partir d'une liste de competence renvoie la competence detaillee'''
    classeur=xlrd.open_workbook(path)
    feuilles=classeur.sheet_names()
    col_code,col_nom_long,col_nom_court=0,1,2
    for f in feuilles:
        if "Competences" in f:
            fs=classeur.sheet_by_name(f)
            k=1
            nom_court=[]
            nom_long=[]
            code_competence=[]
            while fs.cell_value(k,0)!='fin':
                if fs.cell_value(k,col_code) in competences and fs.cell_value(k,col_code)!='':
                    nom_court.append(fs.cell_value(k,col_nom_court))
                    nom_long.append(fs.cell_value(k,col_nom_long))
                    code_competence.append(fs.cell_value(k,col_code))
                k+=1
    return code_competence,nom_long,nom_court
    
        
def genere_support(rep,info_activite,type_activite):
    '''A partir d'une activite genere le fichier support'''
    if type_activite=='cours':
        chemin_relatif='../../'
    elif type_activite=='tp':
        chemin_relatif='../../../Informatique/Exercices/'
    elif type_activite=='ds':
        chemin_relatif='../../'
    if type_activite=='ds':
        (num_ds_str,name_activite,supports,ref_cours,n_cycle,date)=info_activite
        num_activite=num_ds_str
        competences=''
        name_cycle=n_cycle
        num_chapitre=trouver_chapitre(ref_cours)
        date=convdate(date)
        figures=''
    else:
        (date,n_cycle,num_activite,name_cycle,name_activite,supports,competences,figures,ref_cours)=info_activite
        #rep=trouver_repertoire(info_activite) 
        num_chapitre=trouver_chapitre(ref_cours)
    if type_activite=='cours':
        rep_activite=rep+sep+'td.tex'
        rep_activite_cor=rep+sep+'td_cor.tex'
        os.system(copy+''+rep_activite+' '+rep_activite_cor)
        # print(num_activite,rep_activite,supports)
    elif type_activite=='tp':
        rep_activite=rep+'tp.tex'
        rep_activite_cor=rep+'tp-cor.tex'
        #pdb.set_trace()
    elif type_activite=='ds':
        rep_activite=rep+sep+'ds.tex'
        rep_activite_cor=rep+sep+'ds-cor.tex'
    with open(rep_activite,'w',encoding='utf-8') as f:
        if len(supports)>0:
            if type_activite=='cours':
                f.write('\\section{Applications}\n')
            # if type_activite=='tp':
            #     f.write('\\setcounter{section}{'+str(int(num_activite)-1)+'}\n')
            #     f.write('\\section{TP '+num_activite+'}\n')
            if type_activite=='tp' or type_activite=='ds' or type_activite=='cours':
                f2=open(rep_activite_cor,'w',encoding='utf-8')
                f2.write('\n\\vspace{0.1cm}\n\\begin{huge}\n Proposition de corrigé\n\\end{huge}\n\n')
            for support in supports.split(';'):
                if type_activite=='cours':
                    exo,source=trouve_exo_source(support)
                    support_cor=support.split('.tex')[0]+'-cor.tex'
                    f.write('\\subsection{'+exo+'}\n')
                    f.write('\\setcounter{thequestion}{0}\n')
                    f.write('\\input{'+chemin_relatif+support+'}\n')
                    f2.write('\\subsection{'+exo+'}\n')
                    f2.write('\\setcounter{thequestion}{0}\n')
                    if os.path.exists(support_cor):
                        f2.write('\\input{'+chemin_relatif+support_cor+'}\n')
                elif type_activite=='tp' or type_activite=='ds':
                    if support[:2]=='F:':
                        support=support[2:]
                        prefixe_activite=' (Facultative) '
                    else:
                        prefixe_activite=''
                    exo,source=trouve_exo_source(support)
                    support_cor=support.split('.tex')[0]+'-cor.tex'
                    if type_activite=='tp':
                        type_support='activite'
                    elif type_activite=='ds':
                        type_support='exo'
                    if 'consignes' not in support:
                        f.write('\n\n\\'+type_support+'{'+prefixe_activite+exo+'}\n\n')
                        f2.write('\n\n\\'+type_support+'{'+exo+'}\n\n')
                    else:   
                        f.write('\n\n\\noindent\\textbf{Consignes}\n\n')
                    if os.path.exists('../Informatique/Exercices/'+support_cor):
                        f2.write('\\input{'+chemin_relatif+support_cor+'}\n')
                    f.write('\\input{'+chemin_relatif+support+'}\n')
            if type_activite=='tp':
                f2.close()
        else:
            f.write('\n')
        
    return None

# type_activite='tp'
# info_activite=info_tp[0]
# (date,n_cycle,num_activite,name_cycle,name_activite,supports,competences,figures,ref_cours)=info_activite
# rep=trouver_repertoire(info_activite) 
# num_chapitre=trouver_chapitre(ref_cours)
# if type_activite=='cours':
#     rep_activite=rep+'/Cy_0'+str(n_cycle)+'_Ch_0'+str(num_chapitre)+'_TD_'+num_activite
# elif type_activite=='tp':
#     rep_activite=rep+'/Cy_0'+str(n_cycle)+'_Ch_0'+str(num_chapitre)+'_TP_'+num_activite
# with open(rep_activite+'/tp.tex','w',encoding='utf-8') as f:
#     for support in supports.split(';'):
#         f.write('\\input{'+'../../../exos/'+support+'}\n')
# #     


def trouver_file_tex(activite,rep,type_activite):
    '''Trouve le fichier tex a compiler pour une activite donnee'''
    (date,n_cycle,num_activite,name_cycle,name_activite,supports,competences,figures,ref_cours)=activite
    if type_activite=='cours':
        file_tex=rep+sep+'Cy_0'+str(n_cycle)+'_Livret_Ch_'+num_activite+'.tex'
    elif type_activite=='td':
        file_tex=rep+sep+'Cy_0'+str(n_cycle)+'_Ch_'+num_activite+'_TD_'+num_activite+'_cor_PDF.tex'
    elif type_activite=='tp':
        file_tex=rep+'TP'+num_activite+'_pdf.tex'
    return file_tex
    
    
def trouver_file_tex0(activite,rep,type_activite):
    '''Trouve le fichier tex a compiler pour une activite donnee'''
    (date,n_cycle,num_activite,name_cycle,name_activite,supports,competences,figures,ref_cours)=activite
    if type_activite=='cours':
        file_tex=rep+sep+'Cy_0'+str(n_cycle)+'_Livret_Ch_'+num_activite+'.tex'
    elif type_activite=='td':
        file_tex=rep+sep+'Cy_0'+str(n_cycle)+'_Ch_'+num_activite+'_TD_'+num_activite+'_cor_PDF.tex'
    elif type_activite=='tp':
        num_chap=ref_cours.split(';')[0].split('-')[1]
        if int(num_chap)<10 and len(num_chap)<2:
            num_chap='0'+num_chap
        file_tex=rep+sep+'Cy_0'+str(n_cycle)+'_Ch_'+num_chap+'_TP_'+num_activite+sep+'Cy_0'+str(n_cycle)+'_Ch_'+num_chap+'_TP_'+num_activite+'_pdf.tex'
    return file_tex

def compile_tex_python(file_abrege):
    ###pythontex
    # os.system('/usr/local/texlive/2017/bin/x86_64-darwin/pythontex '+file_abrege+'.tex')
    # os.system('/usr/local/texlive/2017/bin/x86_64-darwin/pdflatex '+file_abrege+'.tex')
    # os.system('/usr/local/texlive/2017/bin/x86_64-darwin/pythontex '+file_abrege+'.tex')
    # os.system('/usr/local/texlive/2017/bin/x86_64-darwin/pdflatex '+file_abrege+'.tex')
    # os.system('/usr/local/texlive/2017/bin/x86_64-darwin/pythontex '+file_abrege+'.tex')
    ####pdflatex
    os.system(cmd_latex+file_abrege+'.tex')
    os.system(cmd_latex+file_abrege+'.tex')
    
    
def genere_pdf(file,rep,type_activite):
    '''genere le pdf avec le fichier complet et incomplet'''
    file_abrege=file.split('.')[0].split('/')[-1]
    if type_activite=='cours' or type_activite=='td':
        rep_activite=rep
    elif type_activite=='tp':
        rep_activite=rep
    elif type_activite=='ds':
        rep_activite=rep
    #pdb.set_trace()
    os.chdir(path_ref+sep+rep_activite)
    os.system(rm+'*'+'.aux')
    os.system(rm+'*'+'.log')
    os.system(rm+'*'+'.out')
    os.system(rm+'*'+'.gz')
    os.system(rm+'*'+'.toc')
    os.system(rm+'*'+'.pytxcode')
    os.system(rm+'*'+'.nav')
    os.system(rm+'*'+'.snm')
    os.system(rm+'*'+'.pdf')
    compile_tex_python(file_abrege)
    if type_activite=='tp'or type_activite=='ds':
        compile_tex_python(file_abrege+'-cor')
    # os.system('/usr/local/texlive/2017/bin/x86_64-darwin/pdflatex '+file)
    #pdb.set_trace()
    if type_activite=='ds':
        # os.system('mv '+file_abrege+'.pdf '+path_site_ds+sep+file_abrege+'.pdf')
        shutil.move(file_abrege+'.pdf',path_site_ds+sep+file_abrege+'.pdf')
    #else:
        # os.system('cp '+file_abrege+'.pdf '+path_ref+sep+path_site+sep+file_abrege+'.pdf')
        #shutil.copy(file_abrege+'.pdf',path_ref+sep+path_site+sep+file_abrege+'.pdf')
    if type_activite=='tp':
        # os.system('cp '+file_abrege+'-cor.pdf '+path_ref+sep+path_site+sep+file_abrege+'-cor.pdf')
        #pdb.set_trace()
        shutil.copy(file_abrege+'-cor.pdf',path_ref+sep+path_site+sep+file_abrege+'-cor.pdf')
        shutil.copy(file_abrege+'.pdf',path_ref+sep+path_site+sep+file_abrege+'.pdf')
        print('ras')
    elif type_activite=='ds':
        # os.system('mv '+file_abrege+'-cor.pdf '+path_site_ds+sep+file_abrege+'-cor.pdf')
        shutil.move(file_abrege+'-cor.pdf',path_site_ds+sep+file_abrege+'-cor.pdf')
        os.system(rm+'*'+'.aux')
        os.system(rm+'*'+'.log')
        os.system(rm+'*'+'.out')
        os.system(rm+'*'+'.toc')
        os.system(rm+'*'+'.pytxcode')
        os.system(rm+'*'+'.nav')
        os.system(rm+'*'+'.snm')
        os.system(rm+'*'+'.pdf')
        os.system(rm+'*'+'.idx')
        os.system(rm+'*'+'.bcf')
        os.system(rm+'*'+'.xml')
    # os.system('cp '+file.split('.')[0]+'_complet.pdf '+path_site+sep+file_abrege+'_complet.pdf ')
    # 
    
def genere_pdf0(file,rep,type_activite):
    '''genere le pdf avec le fichier complet et incomplet'''
    file_abrege=file.split('.')[0].split('/')[-1]
    if type_activite=='cours' or type_activite=='td':
        rep_activite=rep
    elif type_activite=='tp':
        rep_activite=rep+sep+file_abrege.split('_pdf')[0]
    elif type_activite=='ds':
        rep_activite=rep
    os.chdir(path_ref+sep+rep_activite)
    os.system(rm+'*'+'.aux')
    os.system(rm+'*'+'.log')
    os.system(rm+'*'+'.out')
    os.system(rm+'*'+'.gz')
    os.system(rm+'*'+'.toc')
    os.system(rm+'*'+'.pytxcode')
    os.system(rm+'*'+'.nav')
    os.system(rm+'*'+'.snm')
    os.system(rm+'*'+'.pdf')
    compile_tex_python(file_abrege)
    if type_activite=='tp'or type_activite=='ds':
        compile_tex_python(file_abrege+'-cor')
    # os.system('/usr/local/texlive/2017/bin/x86_64-darwin/pdflatex '+file)
    #pdb.set_trace()
    if type_activite=='ds':
        # os.system('mv '+file_abrege+'.pdf '+path_site_ds+sep+file_abrege+'.pdf')
        shutil.move(file_abrege+'.pdf',path_site_ds+sep+file_abrege+'.pdf')
    else:
        # os.system('cp '+file_abrege+'.pdf '+path_ref+sep+path_site+sep+file_abrege+'.pdf')
        shutil.copy(file_abrege+'.pdf',path_ref+sep+path_site+sep+file_abrege+'.pdf')
    if type_activite=='tp':
        # os.system('cp '+file_abrege+'-cor.pdf '+path_ref+sep+path_site+sep+file_abrege+'-cor.pdf')
        shutil.copy(file_abrege+'-cor.pdf',path_ref+sep+path_site+sep+file_abrege+'-cor.pdf')
    elif type_activite=='ds':
        # os.system('mv '+file_abrege+'-cor.pdf '+path_site_ds+sep+file_abrege+'-cor.pdf')
        shutil.move(file_abrege+'-cor.pdf',path_site_ds+sep+file_abrege+'-cor.pdf')
        os.system(rm+'*'+'.aux')
        os.system(rm+'*'+'.log')
        os.system(rm+'*'+'.out')
        os.system(rm+'*'+'.toc')
        os.system(rm+'*'+'.pytxcode')
        os.system(rm+'*'+'.nav')
        os.system(rm+'*'+'.snm')
        os.system(rm+'*'+'.pdf')
        os.system(rm+'*'+'.idx')
        os.system(rm+'*'+'.bcf')
        os.system(rm+'*'+'.xml')
    # os.system('cp '+file.split('.')[0]+'_complet.pdf '+path_site+sep+file_abrege+'_complet.pdf ')
    # 
  
def impr_2_page(activite,rep,type_activite):
    os.chdir(path_ref)
    #pdb.set_trace()
    file=trouver_file_tex(activite,rep,type_activite)
    file=file.split('/')[-1]
    file=file.split('.tex')[-2]+'-cor.pdf'
    instr='/Library/TeX/texbin/pdfjam --batch --nup 2x1 --suffix 2up --landscape --outfile . '+file
    print('cd '+path_ref+sep+path_site)
    print(instr)
    
def lire_planning_ds(path):
    """a partir d'une feuille excel correspondant à la progression  des ds renvoie une liste de tuple donnant des colles : (date,cycle,numero,nom du cycle,nom du document, supports d'application pour le ds)"""
    #Ouverture de la progression excel
    classeur=xlrd.open_workbook(path)
    feuilles=classeur.sheet_names()
    
    #Ouverture de la feuille du semanier
    info_ds=[]
    col_data=2#Numero des colonnes des donnees
    #Gestion des ds
    for f in feuilles:
        fs=classeur.sheet_by_name('Planning DS')
    k=1
    num_ds=1
    while fs.cell_value(k,0)!='fin':
        titre=fs.cell_value(k+0,col_data)
        supports=fs.cell_value(k+1,col_data)
        #pdb.set_trace()
        chapitres=fs.cell_value(k+2,col_data)
        cycles=fs.cell_value(k+3,col_data)
        date_ds=fs.cell_value(k+4,col_data)
        if num_ds<10:
            num_ds_str='0'+str(num_ds)
        else:
            num_ds_str=str(num_ds)
        info_ds.append((num_ds_str,titre,supports,chapitres,cycles,date_ds))
        num_ds+=1
        k+=5
    return info_ds
    
def creer_dossier_tp(num_tp):
    nom_dossier='S1_Themes'+sep+'TP'+num_tp+sep
    if os.path.exists(nom_dossier)==False:
        os.mkdir(nom_dossier)
    return nom_dossier
  #######
#Programme Principal
#######

(info_tp,info_cours)=lire_semanier(path)


####Traiter cours
# for cours in info_cours:
#     (date,n_cycle,num_activite,name_cycle,name_activite,supports,competences,figures,ref_cours)=cours
#     rep=trouver_repertoire(cours)
#     genere_fichiers_tex(cours,'cours')
#     genere_entete(rep,cours,'cours')
#     genere_support(rep,cours,'cours')
#     #print(trouver_file_tex(cours,'cours'))


####Traiter TP en générant les .tex
#for tp in info_tp[1:2]:
for tp in info_tp:
     (date,n_cycle,num_activite,name_cycle,name_activite,supports,competences,figures,ref_cours)=tp
     rep=creer_dossier_tp(num_activite)
#     rep=trouver_repertoire(tp)
     genere_fichiers_tex(tp,'tp',rep)
     genere_entete(rep,tp,'tp')
     genere_support(rep,tp,'tp')
#     #print(trouver_file_tex(tp,'tp'))


####Triater DS : gérer dans dropbox
# info_ds=lire_planning_ds(path)   
# for ds in info_ds:
#     (num_ds_str,titre,supports,chapitres,cycles,date_ds)=ds
#     rep='DS/DS'+num_ds_str
#     if os.path.exists(rep)==False:
#         os.mkdir(rep)
#     genere_fichiers_tex(ds,'ds')
#     genere_entete(rep,ds,'ds')
#     genere_support(rep,ds,'ds')

####Compiler tp
#for k in range(len(info_tp)):
###
for k in range(1,3):
    activite=info_tp[k]
    #rep=trouver_repertoire(activite)
    num_tp=activite[2]
    rep=creer_dossier_tp(num_tp)
    file=trouver_file_tex(activite,rep,'tp')
    #genere_pdf(file,rep,'tp')
    #impr_2_page(activite,rep,'tp')
    os.chdir(path_ref)


#####Compliler cours et td
# for k in range(18,19)
#     os.chdir(path_ref)
#     activite=info_cours[k]
#     rep=trouver_repertoire(activite)
#     file=trouver_file_tex(activite,rep,'cours')
#     genere_pdf(file,rep,'cours')
#     file_td=trouver_file_tex(activite,rep,'td')
#     genere_pdf(file_td,rep,'td')

# activite=info_ds[1]
# num_ds_str=activite[0]
# rep='DS/DS'+num_ds_str
# file=rep+sep+'DS'+num_ds_str+'.tex'
# genere_pdf(file,rep,'ds')
#impr_2_page(activite,'tp')


    
#Commande compilation 
#pdflatex Cy_01_livret_Ch_02.tex
#ythontex Cy_01_livret_Ch_02.tex
#pdflatex Cy_01_livret_Ch_02.tex

os.chdir(path_ref)

