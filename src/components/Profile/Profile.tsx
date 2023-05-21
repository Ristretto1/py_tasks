import React from 'react';
import {Posts} from "./Posts/Posts";
import {ProfileInfo} from "./ProfileInfo/ProfileInfo";
import {PostType} from "../../index";

type ProfilePropsType = {
    posts: PostType[]
}

export const Profile = (props: ProfilePropsType) => {
    return (
        <div>
            <ProfileInfo/>
            <Posts posts={props.posts}/>
        </div>
    );
}