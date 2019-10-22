# Run under PoseFlow folder

# Use bash xx.sh to run the if condition sentences
## !!!!! conda activate poseflow !!!!! ##

# # For several cam folders
# for exp in /mnt/Data/CLASP-Activity-Dataset/clasp_2_testdata/*; do
#  for image_dir in $exp/*; do
#   if [[ $image_dir = *_res ]]
#    then
#     echo 'Not this folder'
#    else
#     echo $image_dir
#     results_dir=$image_dir'_res'
#     render_dir=$image_dir'_res_render'
#     python tracker-general.py --imgdir $image_dir \
#                           --in_json $results_dir/alphapose-results.json \
#                           --out_json $results_dir/alphapose-results-forvis-tracked.json \
#                         #   --visdir $render_dir
#   fi
#  done
# done

# For just one cam folder
for image_dir in /mnt/Data/CLASP-Activity-Dataset/20190930/*; do
 if [[ $image_dir = *_res ]]
   then
     echo 'Not this folder'
   else
     echo $image_dir
     results_dir=$image_dir'_res'
     render_dir=$image_dir'_res_render'
     python tracker-general.py --imgdir $image_dir \
                         --in_json $results_dir/alphapose-results.json \
                         --out_json $results_dir/alphapose-results-forvis-tracked.json \
                       #   --visdir $render_dir
 fi
done