import React from 'react';
import {Post} from "./Post/Post";

export const Posts = () => {
    return (
        <div>
            <h3>My posts</h3>
            <div style={{marginBottom: '15px'}}>
                <div>
                    <textarea></textarea>
                </div>
                <button>add post</button>
            </div>
            <div>
                <Post text={'Kirill'}/>
                <Post text={'Tayson'}/>
            </div>
        </div>
    );
};
