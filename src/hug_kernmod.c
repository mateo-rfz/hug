#include <linux/module.h>
#include <linux/init.h>

#define DEVICE_NAME "hug"


static struct file_operations fops = 
{
    .read = NULL,
    .write = NULL
};

static int major;



static int __init hug_init (void) 
{
    printk(KERN_INFO "hug : module loaded\n");
    major = register_chrdev(0 , "hug" , &fops);

    if (major < 0)
    {
        printk(KERN_ERR "hug : module cant create char device on %d\n" , major);
        return -1;
    }
    printk(KERN_INFO "registered successfully with major number %d" , major);
    return 0;
}






static void __exit hug_exit (void) 
{
    unregister_chrdev(major , DEVICE_NAME);
    printk(KERN_INFO "hug : module unloaded\n");
}







module_init(hug_init);
module_exit(hug_exit);



MODULE_LICENSE("GPL");
MODULE_AUTHOR("mateo-rfz");
MODULE_DESCRIPTION("module for hug github.com/mateo-rfz/hug");
