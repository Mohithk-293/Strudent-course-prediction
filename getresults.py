import pickle
import math
def read_dataset():
	global dataset
	with open("./m_d.pkl","rb") as f:
		dataset = pickle.load(f)
	print("Dataset read successfully")
        
def euclidean_distance(sample, list_of_lists):
    distances = {}
    
    for index, lst in enumerate(list_of_lists):
        sample=[float(i) for i in sample]
        lst[:2]=[float(i) for i in lst[:2]]
        if len(sample) != len(lst[:2]):
            raise ValueError("Sample and lists in the list of lists must have the same dimension.")
        
        # Compute the Euclidean distance between the sample and the current list
        distance = math.sqrt(sum((x - y) ** 2 for x, y in zip(sample, lst[:2])))
        
        distances[index] = distance
    
    return distances
	
def get_nearest_lists(distances, list_of_lists, k=10, num_elements=3):
    # Sort distances dictionary based on increasing distances
    sorted_distances = sorted(distances.items(), key=lambda x: x[1])
    
    # Get the indices of the lists for the first k nearest distances
    nearest_indices = [index for index, _ in sorted_distances[:k]]
    
    # Get the first 'num_elements' elements from each of the nearest lists
    nearest_elements = [list_of_lists[index][:num_elements] for index in nearest_indices]
    
    return nearest_elements

def predict_course(sample,c):
    distances=euclidean_distance(sample,dataset)
    nearest_neighbor=get_nearest_lists(distances,dataset,k=len(dataset))
    courses=[]
    print('Predicted courses: ')
    n=0
    for i in nearest_neighbor:
            if (i[-1] not in courses):
                courses.append(i[-1])
                print(i[-1])
                n+=1
                if (n==c):
                    break
    return courses            
read_dataset()