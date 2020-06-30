def crop(name, arr):
    H,W,_ = arr.shape
    if name.split('.')[0][-1]=='L':
        f_arr = arr[:,:W//2,:]
    else:
        f_arr = arr[:,W//2:,:]
    H,W,_ = f_arr.shape
    h_c = int(np.ceil(H*0.05))
    w_c = int(np.ceil(W*0.05))
    return f_arr[ h_c:-1*h_c , w_c:-1*w_c , : ]