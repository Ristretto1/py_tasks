import React from 'react';

type PostPropsType = {
    text: string
    likesCount: number
}

export const Post = (props: PostPropsType) => {
    return (
        <div>
            {props.text}
            <div>
                likes: {props.likesCount}
            </div>
        </div>
    );
};

