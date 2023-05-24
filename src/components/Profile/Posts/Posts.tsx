import React, {LegacyRef} from 'react';
import {Post} from "./Post/Post";
import {PostType} from "../../../types";

type PostsPropsType = {
    posts: PostType[]
}

export const Posts = (props: PostsPropsType) => {
    const mappedPosts = props.posts.map(el => <Post text={el.text} likesCount={el.likesCount} key={el.id}/>)
    const textareaRef: LegacyRef<HTMLTextAreaElement> | undefined = React.createRef()
    const addPost = () => {
            console.log(textareaRef.current?.value)
    }

    return (
        <div>
            <h3>My posts</h3>
            <div style={{marginBottom: '15px'}}>
                <div>
                    <textarea ref={textareaRef} ></textarea>
                </div>
                <button onClick={addPost}>add post</button>
            </div>
            <div>
                {mappedPosts}
            </div>
        </div>
    );
};
