# for exp in /mnt/Data/CLASP-Activity-Dataset/person_info/clasp_2_testdata/*; do
#  for image_dir in exp/*; do
 for image_dir in /mnt/Data/CLASP-Activity-Dataset/person_info/20190930/*; do
  if [[ $image_dir = *_res ]]
   then
    echo $image_dir' Not this folder'
   else
    python interface.py $image_dir 
  fi
 done
# done