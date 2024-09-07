import numpy as np

def allocate_memory():
    memory_chunks = []
    try:
        while True:
            # Allocate a large chunk of memory
            chunk = np.empty((1024 * 1024 * 1, ), dtype=np.uint8)  # 1 MB chunk
            memory_chunks.append(chunk)  # Keep track of the allocated chunk
            
            # Optional: Print status update
            if len(memory_chunks) % 100 == 0:
                print(f"Allocated {len(memory_chunks)} MB")
    except MemoryError:
        print("Memory allocation failed")

if __name__ == "__main__":
    allocate_memory()
