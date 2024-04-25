
from .fancy_print import Message
import time


class FancyIter:
    """
    Parameters
    ----------
    lst : iterable or iterator object (list, range, enumerate, zip, np.array, etc.)
    
    Returns
    -------
        iterator object that prints the progress of the iteration (and the remaining time).
    """
    
    def __init__(self, lst, message:str="Done!",size:int=None)->None:
        
        try:
            if size is None:
                self.max = len(lst)
            else:
                self.max = size
                
            self.list = lst.__iter__()
        except:
            Message(f"Warning: unable to iterate over the object of type {type(lst)}. This may be because it is an iterator without a __len__ magic method. In this case, you can provide an argument 'size'. Trying to convert to list...")
            lst = list(lst)
            self.max = len(lst)
            self.list = lst.__iter__()
        
        self.count = 0
        self.start_time = time.time()
        
        self._previous_print = ""
        self._previous_time = self.start_time
        self.message = message + " " * 30
        
        self.muted = Message.muted
        self._close_channel()
    
    def __iter__(self):
        return self
    
    def __next__(self):
        
        self.show_progress()
        self.update_progress()
        
        try:
            return next(self.list)
        except StopIteration:
            self._open_channel()
            Message(self.message)
            raise StopIteration()
    
    def update_progress(self):
        self.count += 1
    
    def show_progress(self):    
        if not self.muted:
            next_print = f"[{round(self.count/self.max * 100):02d}%]"
            
            if (next_print != self._previous_print) or (time.time() - self._previous_time > 1): # update at least every 10 seconds

                if self.count == 0:
                    time_info = "Time remaining: \\"
                else:
                    # let's add time information
                    time_of_iteration = (time.time() - self.start_time) / self.count
                    remaining_time = round(time_of_iteration * (self.max - self.count))
                    
                    # lets format the time
                    hours = remaining_time // 3600
                    minutes = (remaining_time % 3600) // 60
                    seconds = remaining_time % 60
                    
                    time_info = f"Time remaining: {hours:02d}:{minutes:02d}:{seconds:02d}"
                
                
                
                    print(f"{next_print} {time_info}",end="\r")
                    self._previous_time = time.time()
                    self._previous_print = next_print
        
        
    def _close_channel(self)->None:
        """
        Mutes the messages, so that nothing gets printed during the iteration.
        Without this, othe rmessages might get in the way of the progress bar.
        """
        Message.mute()
        
    def _open_channel(self)->None:
        """
        Undo _close_channel(). Checks if Message was already muted before the start of the iteration. If so, it won't unmute it.
        """
        if not self.muted:
            Message.unmute()
                    

    