spark-submit\
   --master local\
   --deploy-mode client\
   src/run.py True \ 

res=$?
echo "Job finished with status" $res
exit $res
