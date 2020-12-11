spark-submit\
   --master local\
   --deploy-mode client\
   src/run.py $1 \ 

res=$?
echo "Job finished with status" $res
exit $res
