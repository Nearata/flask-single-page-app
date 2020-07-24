import m from "mithril";

const Layout = {
    view: vnode => {
        return [
            m("main.layout", [
                m("nav.menu", [
                    m(m.route.Link, {href: "/"}, "Users")
                ]),
                m("section", vnode.children)
            ])
        ]
    }
}
export default Layout;