"""A video player class."""

from .video_library import VideoLibrary
from .playlist import Playlist
import random
import copy


class VideoPlayer:
    """A class used to represent a Video Player."""

    def __init__(self):
        self._video_library = VideoLibrary()
        self.current_video = 0
        self.current_info = 0
        self.pause = False
        self.playlist = {}

    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos())
        print(f"{num_videos} videos in the library")

    def show_all_videos(self):
        """Returns all videos."""

        print("Here's a list of all available videos: ")
        
        """Set up to display correctly"""
        video_id= self._video_library.get_video_id()
        names = []
        info = []
        tag = []
        for x in range(len(video_id)):
            location = self._video_library.get_video(video_id[x])
            title = location.title
            info_id = location.video_id
            tags = location.tags
            tag_str = ""
            for y in range(len(tags)):
                if y == len(tags)-1:
                    tag_str += ""+str(tags[y])+""
                else:
                    tag_str += ""+str(tags[y])+" "
            names.append(title)
            info.append(info_id)
            tag.append(tag_str)
        
        """To display in the alphabetical order"""
        names2 = copy.copy(names)   
        names2.sort()
        for i in range(len(names)):
            x = names.index(names2[i])
            
            print("   "+names[x]+" ("+info[x]+") ["+tag[x]+"]")

    def play_video(self, video_id):
        """Plays the respective video.

        Args:
            video_id: The video_id to be played.
        """
        self.current_info = self._video_library.get_video(video_id)
        
        
        """Check whether video exist or already playing"""
        if self.current_info == None:
            print("Cannot play video: Video does not exist")
            self.current_video = 0
        
        elif self.current_video == 0:
            self.current_video = self.current_info.title
            print("Playing video: "+str(self.current_video)+"")
            self.pause = False
            
        else:
            print("Stopping video: "+str(self.current_video)+"")
            self.current_video = self.current_info.title
            print("Playing video: "+str(self.current_video)+"")
            self.pause = False
            

    def stop_video(self):
        """Stops the current video."""

        if self.current_video == 0:
            print("Cannot stop video: No video is currently playing")
            
        else:
            print("Stopping video: " +str(self.current_video)+"")
            self.current_video = 0


    def play_random_video(self):
        """Plays a random video from the video library."""
        video_id = self._video_library.get_video_id()
        
        """Similar implementation to the above 2 functions"""
        
        if self.current_video == 0:
            index = random.randint(0,len(video_id)-1)
            self.current_info = self._video_library.get_video(video_id[index])
            self.current_video = self.current_info.title
            print("Playing video: "+str(self.current_video)+"")
            self.pause = False

            
        else:
            print("Stopping video: " +str(self.current_video)+"")
            index = random.randint(0,len(video_id)-1)
            self.current_info = self._video_library.get_video(video_id[index])
            self.current_video = self.current_info.title
            print("Playing video: "+str(self.current_video)+"")
            self.pause = False

    def pause_video(self):
        """Pauses the current video."""
        
        """Setting a pause key variable"""

        if self.current_video == 0:
            print("Cannot pause video: No video is currently playing")
        
        elif self.pause == False and self.current_video != 0:
            print("Pausing video: "+str(self.current_video)+"")
            self.pause = True

        elif self.pause == True and self.current_video != 0:
            print("Video already paused: "+str(self.current_video)+"")

    def continue_video(self):
        """Resumes playing the current video."""
        
        if self.current_video == 0:
            print("Cannot continue video: No video is currently playing")
            
        elif self.pause == False and self.current_video != 0:
            print("Cannot continue video: Video is not paused")

        elif self.pause == True and self.current_video != 0:
            print("Continuing video: "+str(self.current_video)+"")
            self.pause = False

    def show_playing(self):
        """Displays video currently playing."""

        if self.current_video == 0:
            print("No video is currently playing")
            
        else: 
            """Suitable display of information"""
            if self.current_video == self.current_info.title:
                title = self.current_info.title
                info_id = self.current_info.video_id
                tags = self.current_info.tags
                tag_str = ""
                for y in range(len(tags)):
                    if y == len(tags)-1:
                        tag_str += ""+str(tags[y])+""
                    else:
                        tag_str += ""+str(tags[y])+" "
                if self.pause == False:
                    print("Currently playing: "+title+" ("+info_id+") ["+tag_str+"]")
                elif self.pause == True:
                    print("Currently playing: "+title+" ("+info_id+") ["+tag_str+"] - PAUSED")
                        

    def create_playlist(self, playlist_name):
        """Creates a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        
        """Case sensitive condition removal"""
        playlist_list = list(self.playlist.keys())
        playlist_list = [element.upper() for element in playlist_list]
        
            
        if playlist_name.upper() in playlist_list:
            print("Cannot create playlist: A playlist with the same name already exists")
            
        else:
            self.playlist[playlist_name] = Playlist(playlist_name, [])
            print("Successfully created new playlist: "+str(playlist_name)+"")
            return self.playlist
                
            
    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.
        """
        playlist_list = list(self.playlist.keys())
        play_index = copy.copy(playlist_list) 
        playlist_list = [element.upper() for element in playlist_list]
        
        if (playlist_name.upper() in playlist_list) == False:
            print("Cannot add video to "+str(playlist_name)+": Playlist does not exist")
            
        else:
            """Search video tool followed by case sensitive tool"""
            x = playlist_list.index(playlist_name.upper())
            playlist_video = self.playlist.get(play_index[x]).video_id
            current_video = self._video_library.get_video(video_id)
            
            if current_video == None:
                print("Cannot add video to "+str(playlist_name)+": Video does not exist")
            
            elif video_id in playlist_video:
                print("Cannot add video to "+str(playlist_name)+": Video already added")
                
            else:
                """Replace new playlist videos with old one"""
                playlist_video.append(video_id)
                self.playlist[playlist_name] = Playlist(playlist_name, playlist_video)
                video_title = current_video.title
                print("Added video to "+str(playlist_name)+": "+str(video_title)+"")
                

    def show_all_playlists(self):
        """Display all playlists."""
        
        playlist_list = list(self.playlist.keys())
        if len(playlist_list) == 0:
            print("No playlists exist yet")
        else:
            print("Showing all playlists:")
            quant = len(playlist_list)
            for x in range(quant):
                print("  "+str(playlist_list[quant-1-x])+"") 
                

    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        
        """Combination of part3 and part 1 implementation"""
        playlist_list = list(self.playlist.keys())
        play_index = copy.copy(playlist_list) 
        playlist_list = [element.upper() for element in playlist_list]
        
        if (playlist_name.upper() in playlist_list) == False:
            print("Cannot show playlist "+str(playlist_name)+": Playlist does not exist")
        
        else:
            x = playlist_list.index(playlist_name.upper())
            playlist_video = self.playlist.get(play_index[x]).video_id
            print("Showing playlist: "+str(playlist_name)+"")
            if len(playlist_video) == 0:
                print("   No videos here yet")
                
            else:
                for x in range(len(playlist_video)):
                    location = self._video_library.get_video(playlist_video[x])
                    title = location.title
                    info_id = location.video_id
                    tags = location.tags
                    tag_str = ""
                    for y in range(len(tags)):
                        if y == len(tags)-1:
                            tag_str += ""+str(tags[y])+""
                        else:
                            tag_str += ""+str(tags[y])+" "
                    print("   "+title+" ("+info_id+") ["+tag_str+"]")
                    
            
    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed.
        """
        
        """Similar to add video but instead of append but remove"""
        """With checks on current playlist, if able to obtain video or is there the video"""
        
        playlist_list = list(self.playlist.keys())
        play_index = copy.copy(playlist_list) 
        playlist_list = [element.upper() for element in playlist_list]
        
        if (playlist_name.upper() in playlist_list) == False:
            print("Cannot remove video from "+str(playlist_name)+": Playlist does not exist")
            
        else:
            x = playlist_list.index(playlist_name.upper())
            playlist_video = self.playlist.get(play_index[x]).video_id
            current_video = self._video_library.get_video(video_id)
            if current_video == None:
                print("Cannot remove video from "+str(playlist_name)+": Video does not exist")
            elif (video_id in playlist_video) == False:
                print("Cannot remove video from "+str(playlist_name)+": Video is not in playlist")
            else:
                playlist_video.remove(video_id)
                self.playlist[playlist_name] = Playlist(playlist_name, playlist_video)
                print("Removed video from "+str(playlist_name)+": "+str(current_video.title)+"")
                    

    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        
        """Similar implementation to add or remove but replacing with an empty list"""
        
        playlist_list = list(self.playlist.keys())
        playlist_list = [element.upper() for element in playlist_list]
        
        if (playlist_name.upper() in playlist_list):
            self.playlist[playlist_name] = Playlist(playlist_name, [])
            print("Successfully removed all videos from "+str(playlist_name)+"")

        else:
            print("Cannot clear playlist "+str(playlist_name)+": Playlist does not exist")

    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        
        """Using dictionary built in function to remove the list"""
        playlist_list = list(self.playlist.keys())
        playlist_list = [element.upper() for element in playlist_list]
        
        if (playlist_name.upper() in playlist_list):
            self.playlist.pop(playlist_name)
            print("Deleted playlist: "+str(playlist_name)+"")
        else:
            print("Cannot delete playlist "+str(playlist_name)+": Playlist does not exist")

    def search_videos(self, search_term):
        """Display all the videos whose titles contain the search_term.

        Args:
            search_term: The query to be used in search.
        """
        
        """Use of lists to display in an appropiate order"""
        characters = list(search_term.upper())
        video_id= self._video_library.get_video_id()
        options = []
        names = []
        play_id = []
        
        """Implementation of checking each term and compare with entered term"""
        """Using break to prevent time consuming process"""
        for x in range(len(video_id)):
            location = self._video_library.get_video(video_id[x])
            title = location.title.upper()
            term = title.split()
            
            for y in range(len(term)):
                check = len(options)
                video_ch = list(term[y])
                
                for z in range(len(characters)):
                    if video_ch[z] != characters[z]:
                        break
                    
                    elif z == len(characters)-1 and video_ch[z] == characters[z]:
                        title = location.title
                        info_id = location.video_id
                        tags = location.tags
                        tag_str = ""
                        for y in range(len(tags)):
                            if y == len(tags)-1:
                                tag_str += ""+str(tags[y])+""
                            else:
                                tag_str += ""+str(tags[y])+" "
                        options.append(""+title+" ("+info_id+") ["+tag_str+"]")
                        names.append(title)
                        play_id.append(info_id)
                        
                if len(options) == check+1:
                    break
        
        """Check whether any result"""
        if len(options) == 0:
            print("No search results for "+search_term+"")
        
        else:
            print("Here are the results for "+search_term+":")
            choice_list = []
            names2 = copy.copy(names)   
            names2.sort()
            for i in range(len(names)):
                x = names.index(names2[i])
                print("   "+str(i+1)+") "+options[x]+"")
                choice_list.append(play_id[x])
                
            print("Would you like to play any of the above? If yes, specify the number of the video.")
            print("If your answer is not a valid number, we will assume it's a no.")
            choice = input("")
            
            if choice.isnumeric() and int(choice) <= len(play_id):
                self.play_video(play_id[int(choice)-1])
            else:
                pass
                

    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag.

        Args:
            video_tag: The video tag to be used in search.
        """
        
        """Similar implementation to the above but with tuple object"""
        characters = list(video_tag.upper())
        video_id= self._video_library.get_video_id()
        options = []
        names = []
        play_id = []
        
        for x in range(len(video_id)):
            location = self._video_library.get_video(video_id[x])
            tag = location.tags
            
            for y in range(len(tag)):
                check = len(options)
                video_ch = list(tag[y].upper())
                
                for z in range(len(characters)):
                    if video_ch[z] != characters[z]:
                        break
                    
                    elif z == len(characters)-1 and video_ch[z] == characters[z]:
                        title = location.title
                        info_id = location.video_id
                        tag_str = ""
                        for y in range(len(tag)):
                            if y == len(tag)-1:
                                tag_str += ""+str(tag[y])+""
                            else:
                                tag_str += ""+str(tag[y])+" "
                        options.append(""+title+" ("+info_id+") ["+tag_str+"]")
                        names.append(title)
                        play_id.append(info_id)
                        
                if len(options) == check+1:
                    break
        
        if len(options) == 0:
            print("No search results for "+video_tag+"")
        
        else:
            print("Here are the results for "+video_tag+":")
            choice_list = []
            names2 = copy.copy(names)   
            names2.sort()
            for i in range(len(names)):
                x = names.index(names2[i])
                print("   "+str(i+1)+") "+options[x]+"")
                choice_list.append(play_id[x])
                
            print("Would you like to play any of the above? If yes, specify the number of the video.")
            print("If your answer is not a valid number, we will assume it's a no.")
            choice = input("")
            
            if choice.isnumeric() and int(choice) <= len(play_id):
                self.play_video(play_id[int(choice)-1])
            else:
                pass
        

    def flag_video(self, video_id, flag_reason=""):
        """Mark a video as flagged.

        Args:
            video_id: The video_id to be flagged.
            flag_reason: Reason for flagging the video.
        """
        print("Trying to complete as much as I can with the given time at actual internship")

    def allow_video(self, video_id):
        """Removes a flag from a video.

        Args:
            video_id: The video_id to be allowed again.
        """
        print("Flagging would be done in free time")
