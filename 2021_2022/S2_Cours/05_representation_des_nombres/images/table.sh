#! /bin/sh

# table B op
# calcul de la table de l'opération op en base B.
#
B=$1
op="$2"

chiffre_max=$(dc -e "$B 1 - p")

# les chiffres écrits en base B :
chiffres=$(seq 0 $chiffre_max | xargs -iX dc -e "$B o X p")

echo -n '\\begin{tabular}{r'
for i in $chiffres; do echo -n 'r'; done
echo '}'
echo '\\toprule'
# première ligne:
echo -n '\\textbf{\\texttt{'"$op"'}}'
for i in $chiffres; do echo -n '&' '\\textbf{\\texttt{'$i'}}'; done
echo '\\\\ \\midrule'
# les autres:
for i in $chiffres
do
  # ligne i
  echo -n '\\textbf{\\texttt{'$i'}}'
  for j in $chiffres
  do
    # calcul avec dc en choisissant la bonne base en entrée et en sortie.
    # Quelle que soit la base B, B s'écrit 10 en base B,
    # d'où l'argument de la commande "o" de dc :
    s=$(dc -e "$B i 10 o $i $j $op p")
    echo -n ' & \\texttt{'$s'}'
  done
  echo '\\\\'
done
echo '\\bottomrule'
echo '\\end{tabular}'

