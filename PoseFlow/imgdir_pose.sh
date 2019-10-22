# Run under PoseFlow folder

## Pose Result, conda activate py37pt101 
cd ..
# for exp in /mnt/Data/CLASP-Activity-Dataset/20190928/*; do 
#  for image_dir in $exp/*; do
 for image_dir in /mnt/Data/CLASP-Activity-Dataset/20190930/*; do
  echo $image_dir
  results_dir=$image_dir'_res'
  render_dir=$image_dir'_res_render'
  python demo.py --indir $image_dir --outdir $results_dir
 done
# done 