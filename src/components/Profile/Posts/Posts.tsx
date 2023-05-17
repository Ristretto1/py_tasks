import React from 'react';
import {Post} from "./Post/Post";

export const Posts = () => {

    const postsData = [
        {id: 1, text: 'kirill', likesCount: 12},
        {id: 2, text: 'Anya', likesCount: 12},
        {id: 3, text: 'Tayson', likesCount: 12},
    ]

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
                {postsData.map(el => <Post text={el.text} likesCount={el.likesCount} key={el.id}/>)}
            </div>
        </div>
    );
};
