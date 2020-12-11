spark-submit\
   --master local\
   --deploy-mode client\
   src/run.py\

res=$?
echo "Job finished with status" $res
exit $res
