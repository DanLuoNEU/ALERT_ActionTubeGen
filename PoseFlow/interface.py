import json
import cv2
import sys


clip_path = sys.argv[1]
json_file = clip_path+'_res/alphapose-results-forvis-tracked.json'
save_path = clip_path+'/persons.json'
bbox_edge = 40
# data : num_img(dictionary){ 
#           keys:img_name, 
#           values: num_cur_persons(dictionary){
#                   'idx', 
#                   'keypoints': 3(x,y,conf) x 17
#                   } 
#       }
with open(json_file) as f:
    data = json.load(f)

persons = {} #bounding boxes dictionary
num_person = 0
# img_list
for img in sorted(data.keys()):
    img_path = clip_path+'_res_render/'
    img_f = cv2.imread(img_path+img+'.png')
    # persons in one image
    for person in data[img]:
        # if new person shows up, extend the dictionary
        if person['idx'] > len(persons):
            persons[person['idx']] = {
                    'img_name': [],
                    'joints': [],
                    'bbox': []}
        # Add data to every person
        persons[person['idx']]['img_name'].append(img)
        persons[person['idx']]['joints'].append(person['keypoints'])
        # According to the joint information to get bounding box
        x_min = person['keypoints'][0]
        x_max = person['keypoints'][0]
        y_min = person['keypoints'][1]
        y_max = person['keypoints'][1]
        for i in range(17-1):
            if person['keypoints'][3*i] > x_max:
                x_max = person['keypoints'][3*i]
            elif person['keypoints'][3*i] < x_min:
                x_min = person['keypoints'][3*i]
            
            if person['keypoints'][3*i+1] > y_max:
                y_max = person['keypoints'][3*i+1]
            elif person['keypoints'][3*i+1] < y_min:
                y_min = person['keypoints'][3*i+1]
            
        bbox = [x_min, y_min, x_max, y_max]
        persons[person['idx']]['bbox'].append(bbox)

        # ########## Test bounding box of tracked.json ##############
        # # draw id and bbox
        # x1 = int(x_min)-bbox_edge
        # y1 = int(y_min)-2*bbox_edge
        # x2 = int(x_max)+bbox_edge
        # y2 = int(y_max)
        # cv2.rectangle(img_f, (x1, y1), (x2, y2), (255, 255, 0), 4)
        # label = f"id: {person['idx']}"
        # cv2.putText(img_f, label,
        #             (x1 + 20, y1 + 40),
        #             cv2.FONT_HERSHEY_SIMPLEX,
        #             1,  # font scale
        #             (255, 0, 255),
        #             2)  # line type

        # cv2.imshow(img, img_f)
        # k = cv2.waitKey(0)
        # # ESC to quit, 'c' to next image
        # if k == 27:
        #     cv2.destroyAllWindows()
        #     exit(0)
        # elif k == ord('n'):
        #     cv2.destroyAllWindows()


# ########## Test bounding box of persons.json ##############
# img_path = ori_path+'_res_render/'
# person_index=1
# for i in range(len(persons[person_index]['img_name'])):
#     img_name = persons[person_index]['img_name'][i]  
#     img = cv2.imread(img_path+img_name+'.png')
#     # draw id and bbox
#     x1 = int(persons[person_index]['bbox'][i][0])-bbox_edge
#     y1 = int(persons[person_index]['bbox'][i][1])-2*bbox_edge
#     x2 = int(persons[person_index]['bbox'][i][2])+bbox_edge
#     y2 = int(persons[person_index]['bbox'][i][3])
#     cv2.rectangle(img, (x1, y1), (x2, y2), (255, 255, 0), 4)
#     #label = f"""{voc_dataset.class_names[labels[i]]}: {probs[i]:.2f}"""
#     label = f"id: 1"
#     cv2.putText(img, label,
#                 (x1 + 20, y1 + 40),
#                 cv2.FONT_HERSHEY_SIMPLEX,
#                 1,  # font scale
#                 (255, 0, 255),
#                 2)  # line type


#     cv2.imshow(img_name, img)
#     k = cv2.waitKey(0)
#     # ESC to quit, 'c' to next image
#     if k == 27:
#         cv2.destroyAllWindows()
#         exit(0)
#     elif k == ord('n'):
#         cv2.destroyAllWindows()
          
# Save the tracking information
with open(save_path, 'w') as outfile:
    json.dump(persons, outfile)

print(clip_path+' Done!')