# PROGRAMMER: Wesley Jacoby
# DATE CREATED: 20 July 2020
# REVISED DATE: 
# PURPOSE: Create the function get_pet_labels that creates the pet labels from 
#          the image's filename. This function inputs: 
#           - The Image Folder as image_dir within get_pet_labels function and 
#             as in_arg.dir for the function call within the main function. 
#          This function creates and returns the results dictionary as results_dic
#          within get_pet_labels function and as results within main. 
#          The results_dic dictionary has a 'key' that's the image filename and
#          a 'value' that's a list. This list will contain the following item
#          at index 0 : pet image label (string).
#
##
# Imports python modules
from os import listdir


def get_pet_labels(image_dir):
    """
    Creates a dictionary of pet labels (results_dic) based upon the filenames 
    of the image files. These pet image labels are used to check the accuracy 
    of the labels that are returned by the classifier function, since the 
    filenames of the images contain the true identity of the pet in the image.
    Be sure to format the pet labels so that they are in all lower case letters
    and with leading and trailing whitespace characters stripped from them.
    (ex. filename = 'Boston_terrier_02259.jpg' Pet label = 'boston terrier')
    Parameters:
     image_dir - The (full) path to the folder of images that are to be
                 classified by the classifier function (string)
    Returns:
      results_dic - Dictionary with 'key' as image filename and 'value' as a 
      List. The list contains for following item:
         index 0 = pet image label (string)
    """
    # Creates list of files in directory
    filename_list = listdir(image_dir)

    # Processes each of the files to create a dictionary where the key
    # is the filename and the value is the picture label (below).
 
    # Creates empty dictionary for the results (pet labels, etc.)
    results_dic = dict()

    for filename in filename_list:
        # Skips file if starts with . (like .DS_Store of Mac OSX) because it 
        # isn't a pet image file
        if filename[0] != '.':
            # Creates temporary label variable to hold pet label name extracted
            pet_label = ''
            # process each filename in the in_files list to extract the dog breed 
            # name from the filename
            pet_image_label = filename.split('.')[0]
            format_pet_image = pet_image_label.lower().split('_')
            
            pet_label = ' '.join([word for word in format_pet_image if word.isalpha()])

        # If filename doesn't already exist in dictionary add it and it's
        # pet label - otherwise print an error message because indicates 
        # duplicate files (filenames)
        if filename not in results_dic:
            results_dic[filename] = [pet_label.strip()]
        else:
            print("** Warning: Duplicate files exist in directory:", filename)

    return results_dic
