import matplotlib.pyplot as plt
import matplotlib.animation as animation
from itertools import count

def swap(A, p1, p2):
    if p1 != p2:
        A[p1], A[p2] = A[p2], A[p1]

def bubblesort(lst):
    N = len(lst)
    if N == 1:
        return

    for i in range(N - 1):     
        for j in range(N-1-i):
            if lst[j] > lst[j+1]:
                swap(lst, j, j+1)             
            yield lst

if __name__ == "__main__":
    
    
    A = [33, 55, 44, 22, 11]

    figure, ax = plt.subplots(figsize=(12,9))
    bar_list = ax.bar(range(len(A)), A, width=0.3, align="edge", color="pink")
    
    index=count()
    def update_figure(A, bars, iteration):
        for bar, value in zip(bars, A):
            bar.set_height(value)
        
    anim = animation.FuncAnimation(figure, func=update_figure,
        fargs=(bar_list, next(index)), frames=bubblesort(A), interval=100,
        repeat=False,save_count=150)
    plt.show()