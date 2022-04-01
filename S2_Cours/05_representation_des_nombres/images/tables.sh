#! /bin/sh

bases='2 8 16'
for b in $bases
do
  sh ./table.sh $b '+' > table-add-$b.tex
  sh ./table.sh $b '*' > table-mul-$b.tex
done
