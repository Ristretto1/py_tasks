import React from 'react';
import {Post} from "./Post/Post";
import {PostType} from "../../../types";

type PostsPropsType = {
    posts: PostType[]
}

export const Posts = (props: PostsPropsType) => {
    const mappedPosts = props.posts.map(el => <Post text={el.text} likesCount={el.likesCount} key={el.id}/>)

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
                {mappedPosts}
            </div>
        </div>
    );
};
