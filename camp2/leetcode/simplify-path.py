class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path + '/'
        def get_answer():
            """
            if it is Empty No need to aappend to the stack and also no need to append . to the stack
            because it represent current-directory name not greater or lesss
            what about .. meaning move one directory up  meaning pop element from stack
            example ---> /home/document/image/school/../..
            ['home', 'document']
            our stack store our simplified directory name 
            we only take care of waay to print the simplified path
            

            if not empty and 
            
            
            """
            
            
            
            N= len(path)
            file_path = ""
            stack = []
            for i in range(N):
                if path[i]=="/":
                    if file_path == '..':
                        if stack:
                            stack.pop()
                    elif file_path!="" and file_path !='.':
                        stack.append(file_path)
                    file_path = ""
                else:
                    file_path +=path[i]
            short_path = "/".join(stack)
            short_path = '/'+ short_path
            return short_path



        return get_answer()
       