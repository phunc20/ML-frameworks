# Motivatoins
People have various reasons for getting motivated to build tensorflow from source.
In my case, around the end of year 2019, I got interested in old thinkpads like x220, x200, etc.
- From x220 on, i.e. x220, x230, x240, etc,  one can easily install tensorflow in python using <code>pip</code>, all versions included.
- But for x200, it's a different story.
    - Seemingly due to CPU structure, the only workable tensorflow versions are those <code><b>tensorflow\<=1.5.0</b></code>; once you go beyond that, you'd get a <code><b>core dump</b></code> message when you try to use tensorflow after <code>pip install</code> it.
    - <code><b>docker</b></code> won't help. <code><b>core dump</b></code> still takes place in docker containers regardless of tf versions.
- Old thinkpad series which have a 32-bit structure e.g. x60, it just seems that people abandoned the idea of running tensorflow on them. In any case, these machine are weak compared to modern standard.


## x200
This is the first use case which motivated me to build tensorflow from source, because I liked x200 so much that I'd like to make it my main laptop.

Not having much knowledge on this, on one hand, I postponed this issue for quite some time;
on the other hand, when I had spared time, I googled to try to solve it little by little.
Eventually I sort of concluded that there are at least two solutions:
01. I uses <code>arch linux</code> on this x200, so this approach might be a little <b>distro-specific</b>
    - <code><b>sudo pacman -S python-tensorflow</b></code> will install tensorflow to the system's default <code>pip</code>/<code>python</code>, which as of 2020/07/18, is <code>python3.8</code>
    - This solution has several drawbacks:
        - It affects the system <code>pip</code> which is not a good practice in python
        - It can only install one version, e.g. version <code>2.2.0rc3-2</code> as of 2020/07/18
02. Build from source
    - Pros
        - All different versions of tensorflow can be built and installed
        - Can be install into an isolated virtual environment
    - Cons
        - Building process takes long


