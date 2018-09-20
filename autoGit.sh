git add .
echo -n "Digite o comentario: "

read comentario                                    
git commit -m "$comentario"
git push

echo "Commit feito!"
