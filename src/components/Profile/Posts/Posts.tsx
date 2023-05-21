import React from 'react';
import {Post} from "./Post/Post";
import {PostType} from "../../../index";

type PostsPropsType = {
    posts: PostType[]
}

export const Posts = (props: PostsPropsType) => {

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
                {props.posts.map(el => <Post text={el.text} likesCount={el.likesCount} key={el.id}/>)}
            </div>
        </div>
    );
};
