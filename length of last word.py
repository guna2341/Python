int lengthOfLastWord(char* s) {
    int i=strlen(s)-1;
    char arr[100][100];
    for(i=strlen(s)-1;i>=0;i--)
    {
        if(s[i]>=65&&s[i]<=122)
        {
            break;
        }
    }
    char res[1000];
    int count=0;
   for(int j=i;j>=0;j--)
   {
    if(s[j]==' ')
    {
        break;
    }
    else
    {
        res[count++]=s[i];
    }
   }
    return strlen(res);
}
