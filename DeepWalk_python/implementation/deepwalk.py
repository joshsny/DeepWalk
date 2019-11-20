# phi represents the matrix of vector embeddings and W represents a walk


def skipgram( phi, W, window_size, learning_rate) :
    for j in len(W):
        v_j = W[j]
        for k in [j - window_size, j + window_size]:
            u_k = W[k]
            J(phi) = -log(P(u_k, phi(j)))
            phi = phi - learning_rate * d_phi
    return

def deepwalk( G, window_size, embedding_size, walks_per_vertex, walk_length) :

