import React, { useState, useEffect } from 'react';
import { Card } from '@/components/ui/card';

const FacebookPublicFeed = () => {
  // 使用 RSS feed 或公開的 oEmbed 端點
  const [posts, setPosts] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchPosts = async () => {
      try {
        // 方法 1: 使用 Facebook oEmbed
        const url = `https://www.facebook.com/plugins/page.php?href=FANPAGE_URL&tabs=timeline`;
        
        return (
          <iframe
            src={url}
            className="w-full min-h-[500px] border-none overflow-hidden"
            allow="encrypted-media"
          />
        );
        
        // 方法 2: 如果有粉專授權，使用 Graph API
        // const response = await fetch(
        //   `https://graph.facebook.com/v18.0/PAGE_ID/posts?access_token=ACCESS_TOKEN&fields=message,created_time`
        // );
        // const data = await response.json();
        // setPosts(data.data);
        
      } catch (error) {
        console.error('Error fetching posts:', error);
      } finally {
        setLoading(false);
      }
    };

    fetchPosts();
  }, []);

  if (loading) {
    return <div className="p-4">Loading...</div>;
  }

  // 如果使用 Graph API 的呈現方式
  return (
    <div className="w-full max-w-2xl mx-auto p-4">
      {posts.map((post) => (
        <Card key={post.id} className="mb-4 p-4">
          <div className="mb-2 text-sm text-gray-600">
            {new Date(post.created_time).toLocaleDateString()}
          </div>
          <div className="prose">{post.message}</div>
        </Card>
      ))}
    </div>
  );
};

export default FacebookPublicFeed;