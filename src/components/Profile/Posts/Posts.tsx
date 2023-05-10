import React from 'react';
import {Post} from "./Post/Post";

export const Posts = () => {
    return (
        <div>
            My posts
            <div>
                <textarea></textarea>
                <button>add post</button>
            </div>
            <div>
                <Post text={'Kirill'}/>
                <Post text={'Tayson'}/>
            </div>
        </div>
    );
};
