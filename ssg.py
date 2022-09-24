from ssg.site import Site
import typer

def main(source="content", dest="dist"):
    config=dict({source:"source", dest:"dest"})
    Site(config.source, config.dest).build() 
    
    
    
typer.run(main)       