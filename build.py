top_part=open('templates/top.html').read()
bottom_part=open('templates/bottom.html').read()
middle_about=open('docs/aboutmiddle.html').read()
middle_single=open('docs/singlemiddle.html').read()
middle_gallery=open('docs/gallerymiddle.html').read()

main_gallery = top_part + middle_gallery + bottom_part
main_about= top_part + middle_about + bottom_part
main_single=top_part + middle_single + bottom_part

open('gallery.html','w+').write(main_gallery)
open('art.html','w+').write(main_about)
open('single.html','w+').write(main_single)
